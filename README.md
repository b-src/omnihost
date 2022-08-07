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

The current release has been manually tested on a linux machine. You should (probably) be alright if you have:
 * a new enough version of python or the ability to install one with `pyenv`
 * pip
 * [pyenv](https://github.com/pyenv/pyenv)
 * [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

### Dependencies

python v3.10.5 or newer

Instructions in the Installing section assume you are using `pyenv` and `pyenv-virtualenv`

### Installing

Omnihost can be installed from the python package index via pip ([pypi](https://pypi.org/project/omnihost))

As omnihost currently has no dependencies outside of the python standard library, you should be alright installing it in your global python environment if your system python is new enough. Best practice would be to install it in a virtual environment.

Install python v3.10.5 with `pyenv` if your system python uses a different version
```
$ pyenv install 3.10.5
```

Create a virtual environment using `pyenv-virtualenv`
```
pyenv virtualenv 3.10.5 omnihost
```


Activate the venv
```
$ pyenv activate omnihost
```

Install omnihost in the virtual environment
```
$ python3 -m pip install omnihost
```

### Running

Activate your venv
```
$ pyenv activate omnihost
```

Run omnihost
```
$ omnihost -i <gemtext/source/dir> -w <html/output/dir> -o <gemtext/output/dir> -g <gopher/output/dir> -s <stylesheet/path>
```

Arguments:
 * `-i` gemtext source directory path. This argument is required.
 * `-w` html output directory path. This argument is optional. If an html output path is provided, gemtext files will be converted to html and placed in this directory. This directory must be empty.
 * `-o` gemini output directory path. This argument is optional. If a gemini output path is provided, gemtext files will be copied from the source directory to this directory.
 * `-g` gopher output directory path. This argument is optional. At present nothing is done with this argument. Eventually, if a gopher output path is provided, gemtext files will be converted to gophermaps and placed in this directory. This directory must be empty.
 * `-s` stylesheet path. This argument is optional. If a stylesheet path is provided, the stylesheet will be copied to \<html/output/dir>/css/\<stylesheet> and linked to the html pages as css/\<stylesheet>
 
 ## Roadmap
 
 This is roughly ordered by priority except for conversion of gemtext to gophermaps. That's listed first because it's the biggest piece of missing functionality, but I'm planning to shore up the html conversion before adding that in
 
  * Add ability to convert gemtext to gophermaps
  * Add logging
  * Improve error handling, add custom exception types
  * Add automated tests
  * Add support for nested directory structures for both input and output instead of requiring all input files to be in the top level of the input directory
  * Improve formatting of html output to make it nicely human-readable
  * Consider adding a preprocessing step using something like mdbook to allow for for meta control of generated pages. Would allow for things like:
    + stylesheets specified per page
    + titles that aren't dependent on the file name
    + metadata to support things like auto-generation of subject indexes for wikis

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details