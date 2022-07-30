import os
from shutil import copytree
from typing import Optional

from gemtext_parser import GemtextParser
from html_converter import HTMLConverter


class OmniConverter:
    def __init__(self, source_dir: os.PathLike, html_output_dir: Optional[os.PathLike], gemini_output_dir: Optional[os.PathLike], gopher_output_dir: Optional[os.PathLike]) -> None:
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
        # Current limitations:
        # - requires only gemtext files in source dir
        # - all gemtext files must be in top level of source dir
        if not self._convert_to_html and not self._copy_gemini_files and not self._convert_to_gopher:
            # TODO: probably log and quit instead
            raise Exception("Configured to do nothing.")

        # No reason to parse gemtext files if we're only copying them somewhere
        if self._convert_to_html or self._convert_to_gopher:
            for gemtext_file_path in os.listdir(source_dir):
                
                # TODO: does this need to be converted to full absolute path?
                gemlines = self._gemtext_parser.parse_file_to_gemlines(gemtext_file_path)
                
                if self._convert_to_html:
                    html = self._html_converter.convert_gemlines_to_html(gemlines)
                    # TODO: fix file extension
                    with open(os.path.join(self._html_output_dir, gemtext_file_path), mode="x") as f:
                        f.write(html)
                
                if self._convert_to_gopher:
                    pass
                        
        if self._copy_gemini_files:
            copytree(self._source_dir, self._gemini_output_dir)
