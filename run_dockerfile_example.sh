#!/bin/bash -eu
docker run \
    -v <absolute/local/path/to/source/dir>:/home/appuser/gemini_source \
    -v <absolute/local/path/to/css/dir>:/home/appuser/stylesheet_source \
    -v <absolute/local/path/to/html/output/dir>:/home/appuser/html_output \
    -v <absolute/local/path/to/gemini/output/dir>:/home/appuser/gemini_output \
    -v <absolute/local/path/to/gopher/output/dir>:/home/appuser/gopher_output \
    -e OMNIHOST_SOURCE_DIR="/home/appuser/gemini_source" \
    -e OMNIHOST_CSS_TEMPLATE_PATH="/home/appuser/stylesheet_source/styles.css" \
    -e OMNIHOST_HTML_OUTPUT_DIR="/home/appuser/html_output" \
    -e OMNIHOST_GEMINI_OUTPUT_DIR="/home/appuser/gemini_output" \
    -e OMNIHOST_GOPHER_OUTPUT_DIR="/home/appuser/gopher_output" \
    omnihost:latest