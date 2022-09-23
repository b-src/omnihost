# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
### Changed
 - Containerize script
 - Add support for env variables or a config file instead of requiring file paths to be passed on the command line every single time

## [0.3.0] - 2022-09-17

### Changed
 - Add custom exception types to improve error handling
 - Add logging
 
## [0.2.1] - 2022-08-11

### Fixes

 - Fix internal links so that the html pages no longer point to gemini pages
 - Change program name in CLI help output from 'omniconverter' to 'omnihost'

## [0.2.0] - 2022-08-07

### Added

 - A sane deployment process. Omnihost is now available from pypi.org, installable via pip. Instructions for installation and usage have been updated in the README
 - This CHANGELOG!
 
 ### Changed

 - Dependencies are now managed via `poetry`. Project and dev dependencies have been separated and are listed in `[tool.poetry.dependencies]` and `[tool.poetry.dev-dependencies]` respectively. This obviates the need for requirements.txt
 - Updated roadmap in README to reflect changes
 
## [0.1.0] - 2022-08-06

### Added

 - Initial release with basic functionality 
   + Ability to convert gemtext markup files to html
   + Ability to specify a stylesheet to be applied to generated html files
 - Limitations of initial release
   + No ability to generate gophermaps. A gophermap output directory can be specified, but no action will be taken
   + No support for a nested source or output directory structure. All gemtext files to be converted must be at the top level of the input directory
   + Complicated deployment story. v0.1.0 must be cloned from the repo and run directly.
   + Limited error handling
   + No automated tests, all testing so far has been manual on a subset of functionality
   + No logging