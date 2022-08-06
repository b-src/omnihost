# OMNIHOST

A tool for those who would like to host native gemini content in parallel on the web as well as gopherspace.

## Description

Easily convert a directory full of gemtext markup into HTML and (eventually) gophermaps.

This tool is a work it progress. It should not be considered stable before the v1.0.0 release. Breaking changes may occur at any time.

There are still large swaths of functionality that have not been implemented, including but not limited to:
 - a reasonable deployment story
 - the ability to convert gemtext markup to gopher
 - logging
 - any sort of automated tests

See the Roadmap section for a complete list

### Supported platforms

Officially, currently none. Initial release has been manually tested on a linux machine. You should (probably) be alright if you have:
 * a new enough version of python
 * pip
 * `pyenv`
 * `pyenv-virtualenv` 

### Dependencies

python v3.10.5

Instructions in the Installing section assume you are using `pyenv` and `pyenv-virtualenv`

### Installing

This process will change, hopefull soon. For now "installation" and usage looks a lot like development.

clone the repo
```
$ git clone https://github.com/b-src/omnihost.git
```

install python v3.10.5 with `pyenv` if your system python uses a different version
```
$ pyenv install 3.10.5
```

create a virtual environment using `pyenv-virtualenv`
```
pyenv virtualenv 3.10.5 omnihost-3.10.5
```

activate the venv if you don't have pyenv virtualenv-init added to your shell to automatically activate venvs
```
$ pyenv activate omnihost-3.10.5
```

install dependencies in the virtual environment
```
$ python3 -m pip install -r requirements.txt
```

### Running

Currently the only way to run the project is by running main.py with command line arguments

Make sure your virtual environment is active and cd to the omnihost/ directory

Run main.py
```
$ python3 main.py -i <gemtext/source/dir> -w <html/output/dir> -o <gemtext/output/dir> -g <gopher/output/dir> -s <stylesheet/path>
```

Arguments:
 * `-i` gemtext source directory path. This argument is required.
 * `-w` html output directory path. This argument is optional. If an html output path is provided, gemtext files will be converted to html and placed in this directory. This directory must be empty.
 * `-g` gopher output directory path. This argument is optional. At present nothing is done with this argument. Eventually, if a gopher output path is provided, gemtext files will be converted to gophermaps and placed in this directory. This directory must be empty.
 * `-s` stylesheet path. This argument is optional. If a stylesheet path is provided, the stylesheet will be copied to \<html/output/dir>/css/\<stylesheet> and linked to the html pages as css/\<stylesheet>
 
 ## Roadmap
 
 This is roughly ordered by priority except for conversion of gemtext to gophermaps. That's listed first because it's the biggest piece of missing functionality, but I'm planning to shore up the html conversion before adding that in
 
  * Add ability to convert gemtext to gophermaps
  * Improve deployment story
  * Add logging
  * Improve error handling, add custom exception types
  * Add automated tests
  * Use `poetry` to manage dependencies so that dependencies can be listed in `pyproject.toml` instead of `requirements.txt`
  * Separate dev dependencies from actual project dependencies
  * Improve formatting of html output to make it nicely human-readable

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details