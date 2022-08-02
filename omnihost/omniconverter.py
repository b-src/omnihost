import os
from shutil import copytree
from typing import Optional

from gemtext_parser import GemtextParser
from html_converter import HTMLConverter


class OmniConverter:
    def __init__(
        self,
        source_dir: str,
        html_output_dir: Optional[str],
        gemini_output_dir: Optional[str],
        gopher_output_dir: Optional[str],
    ) -> None:
        self._source_dir = source_dir
        self._html_output_dir = html_output_dir
        self._gemini_output_dir = gemini_output_dir
        self._gopher_output_dir = gopher_output_dir
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
            for gemtext_file_path in os.listdir(self._source_dir):

                # TODO: does this need to be converted to full absolute path?
                gemlines = self._gemtext_parser.parse_file_to_gemlines(gemtext_file_path)

                if self._convert_to_html:
                    page_title = self._convert_filename_to_title(gemtext_file_path)
                    html = self._html_converter.convert_gemlines_to_html(
                        gemlines, page_title
                    )
                    # TODO: fix file extension
                    with open(
                        os.path.join(self._html_output_dir, gemtext_file_path), mode="x"  # type: ignore
                    ) as f:
                        f.write(html)

                if self._convert_to_gopher:
                    pass

        if self._copy_gemini_files:
            copytree(self._source_dir, self._gemini_output_dir)  # type: ignore

    def _convert_filename_to_title(self, filename: str) -> str:
        """Assuming a file format of 'file_name_lowercase_with_underscores.gmi',
        convert to 'File Name Lowercase With Underscores'

        requires only one '.' in filename
        """
        # TODO: this is really lazy and hard to read, split into something reasonable
        # instead of a too-clever one-liner
        return " ".join(word.capitalize() for word in filename.split(".")[0].split("_"))
