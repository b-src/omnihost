from dataclasses import dataclass
from enum import Enum, auto


class LineType(Enum):
    TEXT = auto()
    LINK = auto()
    HEADING = auto()
    SUBHEADING = auto()
    SUBSUBHEADING = auto()
    LISTITEM = auto()
    BLOCKQUOTE = auto()
    PREFORMATTED = auto()
    PREFORMATTED_ALT_TEXT = auto()
    END_PREFORMATTED = auto()
    UNINITIALIZED = auto()


class ParseMode(Enum):
    DEFAULT = auto()
    PREFORMATTED = auto()
    EOF = auto()


@dataclass(frozen=True)
class GemLine:
    line_type: LineType
    line_contents: str


class GemtextParser:
    def __init__(self) -> None:
        self._parse_mode = ParseMode.DEFAULT
        self._STATE_TOGGLE_SYMBOL = "```"

    def parse_file_to_gemlines(self, file_path: str) -> list[GemLine]:
        self._parse_mode = ParseMode.DEFAULT
        gemlines: list[GemLine] = []

        with open(file_path, mode="r", encoding="utf-8") as f:
            while self._parse_mode != ParseMode.EOF:
                line = f.readline()
                if not line:
                    self._parse_mode = ParseMode.EOF
                elif self._line_is_empty(line):
                    # blank lines in Gemtext are just for the author's convenience
                    pass
                else:
                    if self._line_toggles_parse_mode(line):
                        self._toggle_parse_mode()
                        if self._parse_mode == ParseMode.PREFORMATTED and len(line) > len(
                            self._STATE_TOGGLE_SYMBOL
                        ):
                            gemlines.append(
                                GemLine(LineType.PREFORMATTED_ALT_TEXT, line[3:])
                            )
                        elif self._parse_mode == ParseMode.DEFAULT:
                            # proceed to the next line if this line closes the preformatted block
                            # text after the "```" will be ignored
                            gemlines.append(GemLine(LineType.END_PREFORMATTED, ""))
                    else:
                        if self._parse_mode == ParseMode.PREFORMATTED:
                            gemlines.append(GemLine(LineType.PREFORMATTED, line))

                        elif self._parse_mode == ParseMode.DEFAULT:
                            gemline = self._parse_default_mode_gemline(line)
                            gemlines.append(gemline)

        return gemlines

    def _line_is_empty(self, line: str) -> bool:
        return line == "\n"

    def _line_toggles_parse_mode(self, line: str) -> bool:
        if len(line) >= 3:
            if line[:3] == self._STATE_TOGGLE_SYMBOL:
                return True

        return False

    def _toggle_parse_mode(self) -> None:
        if self._parse_mode == ParseMode.DEFAULT:
            self._parse_mode = ParseMode.PREFORMATTED
        elif self._parse_mode == ParseMode.PREFORMATTED:
            self._parse_mode = ParseMode.DEFAULT
        else:
            # invalid parse mode, TODO: throw unique exception instead
            raise Exception("Attempted to toggle un-toggleable parse mode.")

    def _parse_default_mode_gemline(self, line: str) -> GemLine:
        """Parse a gemline in default mode. This method assumes:
        * this line does not toggle the parse mode
        * this line is not empty (i.e. "\n")
        * this line is not blank (i.e. "", EOF)
        """
        line_type = LineType.UNINITIALIZED
        line_content = ""
        # Remove trailing '\n
        line = line.rstrip()

        if len(line) >= 3 and line[:3] == "###":
            line_type = LineType.SUBSUBHEADING
            line_content = line[3:]

        elif len(line) >= 2 and line[:2] == "##":
            line_type = LineType.SUBHEADING
            line_content = line[2:]

        elif len(line) >= 1 and line[:1] == "#":
            line_type = LineType.HEADING
            line_content = line[1:]

        elif len(line) >= 2 and line[:2] == "=>":
            line_type = LineType.LINK
            line_content = line[2:]

        elif len(line) >= 2 and line[:2] == "* ":
            line_type = LineType.LISTITEM
            line_content = line[2:]

        elif len(line) >= 1 and line[:1] == ">":
            line_type = LineType.BLOCKQUOTE
            line_content = line[1:]

        else:
            line_type = LineType.TEXT
            line_content = line

        return GemLine(line_type, line_content)
