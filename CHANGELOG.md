# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project (sort of*) adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

\* Sort of meaning that there may be breaking changes in minor releases prior to v1.0.0. The project should not be considered stable until then. Patch releases will still only contain fixes. Minor releases will contain non-breaking changes and could also include breaking changes. I will do my best to call these out in this changelog

## [Unreleased]

 - None

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