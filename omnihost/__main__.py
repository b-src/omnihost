import argparse
import os
from typing import Optional

from omnihost.omniconverter import OmniConverter


def main(argv: Optional[list[str]] = None) -> None:
    arg_parser = argparse.ArgumentParser(
        prog="omniconverter",
        description="Convert gemtext markup to html (and eventually gopher)",
    )
    arg_parser.add_argument(
        "-i",
        "--input",
        dest="source_dir",
        required=True,
        help="The source path for gemtext files to convert.",
    )
    arg_parser.add_argument(
        "-w",
        "--html_dir",
        dest="html_output_dir",
        nargs="?",
        default=None,
        help="The destination path for generated html files.",
    )
    arg_parser.add_argument(
        "-o",
        "--gemini_output_dir",
        dest="gemini_output_dir",
        nargs="?",
        default=None,
        help="The destination path for copied gemtext files.",
    )
    arg_parser.add_argument(
        "-g",
        "--gopher_output_dir",
        dest="gopher_output_dir",
        nargs="?",
        default=None,
        help="The destination path for generated gopher files.",
    )
    arg_parser.add_argument(
        "-s",
        "--css_template",
        dest="css_template_path",
        nargs="?",
        default=None,
        help="The css template to be applied to all html pages.",
    )

    args = arg_parser.parse_args(argv)

    check_args(
        args.source_dir,
        args.html_output_dir,
        args.gemini_output_dir,
        args.gopher_output_dir,
        args.css_template_path,
    )

    omniconverter = OmniConverter(
        args.source_dir,
        args.html_output_dir,
        args.gemini_output_dir,
        args.gopher_output_dir,
        args.css_template_path,
    )

    omniconverter.convert_gemini_files()


def check_args(
    source_dir: str,
    html_output_dir: Optional[str],
    gemini_output_dir: Optional[str],
    gopher_output_dir: Optional[str],
    css_template_path: Optional[str],
) -> None:
    # TODO: unique exception types throughout
    if source_dir == "":
        raise Exception("Empty input dir path provided")
    if not os.path.exists(source_dir):
        raise Exception(f"Gemtext input directory '{source_dir}' does not exist.")
    if not os.listdir(source_dir):
        raise Exception(f"Gemtext input directory '{source_dir}' is empty.")

    if not html_output_dir and not gemini_output_dir and not gopher_output_dir:
        raise Exception(f"No HTML, gemini, or gopher output directories provided")

    check_output_dir(html_output_dir, "HTML output")
    check_output_dir(gemini_output_dir, "Gemtext output")
    check_output_dir(gopher_output_dir, "Gopher output")

    if css_template_path is not None:
        if not os.path.exists(css_template_path):
            raise Exception(f"CSS template {css_template_path} does not exist.")


def check_output_dir(dir_path: Optional[str], dir_name: str) -> None:
    # TODO: unique exception types throughout
    if dir_path is not None:
        if not os.path.exists(dir_path):
            raise Exception(f"{dir_name} directory '{dir_path}' does not exist.")
        if os.listdir(dir_path):
            raise Exception(f"{dir_name} directory '{dir_path}' is not empty.")


if __name__ == "__main__":
    main()
