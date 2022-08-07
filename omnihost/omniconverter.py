import os
from shutil import copy, copytree
from typing import Optional

from omnihost.gemtext_parser import GemtextParser
from omnihost.html_converter import HTMLConverter


class OmniConverter:
    def __init__(
        self,
        source_dir: str,
        html_output_dir: Optional[str],
        gemini_output_dir: Optional[str],
        gopher_output_dir: Optional[str],
        css_template_path: Optional[str],
    ) -> None:
        self._source_dir = source_dir
        self._html_output_dir = html_output_dir
        self._gemini_output_dir = gemini_output_dir
        self._gopher_output_dir = gopher_output_dir
        self._css_template_path = css_template_path
        self._gemtext_parser = GemtextParser()
        self._html_converter = HTMLConverter()
        self._gopher_converter = None

        self._set_conversion_controls()

    def _set_conversion_controls(self) -> None:
        if self._html_output_dir:
            self._convert_to_html = True
        else:
            self._convert_to_html = False

        if self._gemini_output_dir:
            self._copy_gemini_files = True
        else:
            self._copy_gemini_files = False

        if self._gopher_output_dir:
            self._convert_to_gopher = True
        else:
            self._convert_to_gopher = False

    def convert_gemini_files(self) -> None:
        """Perform conversions based on provided arguments.

        Current limitations:
         - requires only gemtext files in source dir
         - all gemtext files must be in top level of source dir

        Arguments are checked initially to make sure there's at least one action to
        perform at this point
        """
        # No reason to parse gemtext files if we're only copying them somewhere
        if self._convert_to_html or self._convert_to_gopher:
            self._copy_stylesheet_to_output()
            css_dest_path = None
            if self._css_template_path is not None:
                css_dest_path = os.path.basename(self._css_template_path)

            for gemtext_file in os.listdir(self._source_dir):
                gemtext_file_path = os.path.join(self._source_dir, gemtext_file)
                gemtext_file_name = os.path.splitext(gemtext_file)[0]

                gemlines = self._gemtext_parser.parse_file_to_gemlines(gemtext_file_path)

                if self._convert_to_html:
                    html_output_path = os.path.join(
                        self._html_output_dir, f"{gemtext_file_name}.html"  # type: ignore
                    )
                    page_title = self._convert_filename_to_title(gemtext_file_name)
                    html = self._html_converter.convert_gemlines_to_html(
                        gemlines, page_title, css_dest_path
                    )
                    # TODO: fix file extension
                    with open(html_output_path, mode="x") as f:
                        f.write(html)

                if self._convert_to_gopher:
                    pass

        if self._copy_gemini_files:
            copytree(self._source_dir, self._gemini_output_dir, dirs_exist_ok=True)  # type: ignore

    def _convert_filename_to_title(self, filename: str) -> str:
        """Assuming a file name format of 'file_name_lowercase_with_underscores',
        convert to 'File Name Lowercase With Underscores'
        """
        return " ".join(word.capitalize() for word in filename.split("_"))

    def _copy_stylesheet_to_output(self) -> None:
        if self._css_template_path is not None:
            css_dest_dir = os.path.join(self._html_output_dir, "css")  # type: ignore
            os.mkdir(css_dest_dir)
            css_dest_path = os.path.join(
                css_dest_dir, os.path.basename(self._css_template_path)
            )
            copy(self._css_template_path, css_dest_path)
