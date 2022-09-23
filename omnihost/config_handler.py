from typing import Optional

class ConfigHandler:
    def __init__(
        self,
        source_dir: Optional[str],
        html_output_dir: Optional[str],
        gemini_output_dir: Optional[str],
        gopher_output_dir: Optional[str],
        css_template_path: Optional[str]
    ) -> None:
        self.source_dir = source_dir
        self.html_output_dir = html_output_dir
        self.gemini_output_dir = gemini_output_dir
        self.gopher_output_dir = gopher_output_dir
        self.css_template_path = css_template_path

        self._check_for_missing_args_in_env()
        self._check_for_missing_args_in_config_file()
        self._final_arg_check()
        
    def _check_for_missing_args_in_env(self) -> None:
        pass
    
    def _check_for_missing_args_in_config_file(self) -> None:
        pass
    
    def _final_arg_check(self) -> None
        if self.source_dir == "":
            raise ArgumentException("Empty input dir path provided")
        if not os.path.exists(self.source_dir):
            raise ArgumentException(f"Gemtext input directory '{source_dir}' does not exist.")
        if not os.listdir(self.source_dir):
            raise ArgumentException(f"Gemtext input directory '{source_dir}' is empty.")

        if not self.html_output_dir and not self.gemini_output_dir and not self.gopher_output_dir:
            raise ArgumentException("No HTML, gemini, or gopher output directories provided")

        self._check_output_dir(self.html_output_dir, "HTML output")
        self._check_output_dir(self.gemini_output_dir, "Gemtext output")
        self._check_output_dir(self.gopher_output_dir, "Gopher output")

        if css_template_path is not None:
            if not os.path.exists(css_template_path):
                raise ArgumentException(f"CSS template {css_template_path} does not exist.")

    def _check_output_dir(self, dir_path: Optional[str], dir_name: str) -> None:
        if dir_path is not None:
            if not os.path.exists(dir_path):
                raise ArgumentException(f"{dir_name} directory '{dir_path}' does not exist.")
            if os.listdir(dir_path):
                raise ArgumentException(f"{dir_name} directory '{dir_path}' is not empty.")


class ArgumentException(Exception):
    """Represents an error with an argument provided via CLI at runtime."""
    pass
