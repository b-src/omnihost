from dataclasses import dataclass
from enum import auto, Enum
from typing import Optional

from gemtext_parser import GemLine, LineType


class HTMLConverterState(Enum):
    DEFAULT = auto()
    PREFORMATTED = auto()
    LIST = auto()


class HTMLConverter:
    def __init__(self) -> None:
        self._state = HTMLConverterState.DEFAULT

    def convert_gemlines_to_html(self, gemlines: list[GemLine]) -> str:
        self._state = HTMLConverterState.DEFAULT
        html_output = ""
        for gemline in gemlines:
            if self._state == HTMLConverterState.DEFAULT:
                if gemline.line_type == LineType.PREFORMATTED_ALT_TEXT:
                    self._start_preformatted_line(alt_text=gemline.line_contents)

                elif gemline.line_type == LineType.PREFORMATTED:
                    self._start_preformatted_line(content=gemline.line_contents)

                elif gemline.line_type == LineType.LISTITEM:
                    self._state = HTMLConverterState.LIST
                    html_output += f"<ul><li>{gemline.line_contents}</li>"

                else:
                    self._convert_default_gemline_to_html

            elif self._state == HTMLConverterState.PREFORMATTED:
                if gemline.line_type == LineType.PREFORMATTED:
                    html_output += f"\n{gemline.line_contents}"

                elif gemline.line_type == LineType.END_PREFORMATTED:
                    self._state = HTMLConverterState.DEFAULT
                    html_output += "</pre>"

            elif self._state == HTMLConverterState.LIST:
                if gemline.line_type == LineType.LISTITEM:
                    html_output += f"<li>{gemline.line_contents}</li>"
                else:
                    html_output += "</ul>"

                    # the duplicate logic below could be eliminated if there was a
                    # separate END_LIST line in the gemline list

                    if gemline.line_type == LineType.PREFORMATTED_ALT_TEXT:
                        self._start_preformatted_line(alt_text=gemline.line_contents)

                    elif gemline.line_type == LineType.PREFORMATTED:
                        self._start_preformatted_line(content=gemline.line_contents)

                    else:
                        self._state = HTMLConverterState.DEFAULT
                        html_output += self._convert_default_gemline_to_html(gemline)

        return html_output

    def _start_preformatted_line(
        self, alt_text: Optional[str] = None, content: Optional[str] = None
    ) -> str:
        self._state = HTMLConverterState.PREFORMATTED
        if not alt_text and not content:
            # TODO: unique exception type
            raise Exception(
                "The start of a preformatted block requires either alt_text or content."
            )
        elif alt_text and content:
            # TODO: unique exception type
            raise Exception(
                "The start of a preformatted block cannot have both alt_text and content."
            )
        elif alt_text:
            return f'<pre alt="{alt_text}">'
        else:
            return f"<pre>{content}"

    def _convert_default_gemline_to_html(self, gemline: GemLine) -> str:
        match gemline.line_type:
            case LineType.TEXT:
                return f"<p>{gemline.line_contents}</p>"
            case LineType.HEADING:
                return f"<h1>{gemline.line_contents}</h1>"
            case LineType.SUBHEADING:
                return f"<h2>{gemline.line_contents}</h2>"
            case LineType.SUBSUBHEADING:
                return f"<h3>{gemline.line_contents}</h3>"
            case LineType.LINK:
                return self._convert_link_to_html(gemline)
            case LineType.BLOCKQUOTE:
                return self._convert_block_quote_to_html(gemline)
            case _:
                raise Exception(
                    f"_convert_default_gemline_to_html() called on invalid LineType {gemline.line_type}."
                )

    def _convert_link_to_html(self, gemline: GemLine) -> str:
        content = gemline.line_contents.strip().split()
        # Assumes that there is a maximum of 1 region of whitespace within link content
        if len(content) > 2:
            # TODO unique exception type
            raise Exception(
                f"Improperly formatted link line: '=>{gemline.line_contents}'."
            )
        elif len(content) == 2:
            return f'<a href="{content[0]}">{content[1]}</a>'
        else:
            return f'<a href="{content[0]}">{content[0]}</a>'

    def _convert_block_quote_to_html(self, gemline: GemLine) -> str:
        """Handle a variable amount of whitespace at the start of a quote line."""
        quote_content = gemline.line_contents.strip()
        return f"<p>&gt; {quote_content}</p>"
