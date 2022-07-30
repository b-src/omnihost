import os

from omniconverter import OmniConverter


# TODO: make these values configurable instead of defined in source
source_dir = os.path.join("path", "to", "source", "dir")
html_output_dir = os.path.join("path", "to", "html", "output", "dir")
gemini_output_dir = os.path.join("path", "to", "gemini", "output", "dir")
gopher_output_dir = os.path.join("path", "to", "gopher", "output", "dir")


def main() -> None:
    omniconverter = OmniConverter(
        source_dir, html_output_dir, gemini_output_dir, gopher_output_dir
    )
    omniconverter.convert_gemini_files()


if __name__ == "__main__":
    main()
