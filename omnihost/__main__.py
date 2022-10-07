import argparse
import logging
import os
import sys
from typing import Optional

from omnihost.config_handler import ConfigHandler, ConfigException
from omnihost.gemtext_parser import GemtextParserException
from omnihost.omniconverter import OmniConverter, OmniConverterException


def main(argv: Optional[list[str]] = None) -> None:
    # Since we are just logging to stdout for now, the message contents are all we need
    logging.basicConfig(format="%(message)s")
    arg_parser = argparse.ArgumentParser(
        prog="omnihost",
        description="Convert gemtext markup to html (and eventually gopher)",
    )
    arg_parser.add_argument(
        "-i",
        "--input",
        dest="source_dir",
        default=None,
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

    config = None
    
    try:
        config = ConfigHandler(
            args.source_dir,
            args.html_output_dir,
            args.gemini_output_dir,
            args.gopher_output_dir,
            args.css_template_path,
        )

        omniconverter = OmniConverter(
            config.source_dir,
            config.html_output_dir,
            config.gemini_output_dir,
            config.gopher_output_dir,
            config.css_template_path,
        )

        omniconverter.convert_gemini_files()
        sys.exit()

    except ConfigException as e:
        logging.error(f"Argument error: {e}")
        sys.exit(1)

    except GemtextParserException as e:
        logging.error(f"Gemtext parsing error: {e}")
        sys.exit(1)

    except OmniConverterException as e:
        logging.error(f"{e}")

    except Exception as e:
        logging.error(f"Unexpected exception occured: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
