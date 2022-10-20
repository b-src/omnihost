# Omnihost

A static site generator for those who would like to host native gemini content in parallel on the web as well as gopherspace.

## Description

Easily convert a directory full of gemtext markup into HTML and (eventually) gophermaps.

This tool is a work it progress. It should not be considered stable before the v1.0.0 release. Breaking changes may occur at any time.

There are still large swaths of functionality that have not been implemented, including but not limited to:
 - the ability to convert gemtext markup to gopher
 - any sort of automated tests

See the Roadmap section for a complete list

### Supported platforms

The current release has been manually tested on a linux machine. You should (probably) be alright if you have:
 * a new enough version of python or the ability to install one with `pyenv`
 * pip
 * [pyenv](https://github.com/pyenv/pyenv)
 * [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

Omnihost is also available as a docker image.

### Dependencies

python v3.10.5 or newer

OR

docker

### Installing

Omnihost can be installed from the python package index via pip ([pypi](https://pypi.org/project/omnihost))

```
 $ pip install omnihost
```

If you would prefer using the docker image instead of installing via pip, see the Running with Docker section below.

### Running

Run omnihost
```
 $ omnihost -i <gemtext/source/dir> -w <html/output/dir> -o <gemtext/output/dir> -g <gopher/output/dir> -s <stylesheet/path>
```

Because the typical workflow involves running the software with the same arguments every time, there are alternative methods to provide these parameters: environment variables and a config file. If an argument is listed as required below, that means that it is required to be set, not that it must be passed in through the command line.

Arguments:
 * `-i` gemtext source directory path. This argument is required.
 * `-w` html output directory path. This argument is optional. If an html output path is provided, gemtext files will be converted to html and placed in this directory. This directory must be empty.
 * `-o` gemini output directory path. This argument is optional. If a gemini output path is provided, gemtext files will be copied from the source directory to this directory.
 * `-g` gopher output directory path. This argument is optional. At present nothing is done with this argument. Eventually, if a gopher output path is provided, gemtext files will be converted to gophermaps and placed in this directory. This directory must be empty.
 * `-s` stylesheet path. This argument is optional. If a stylesheet path is provided, the stylesheet will be copied to \<html/output/dir>/css/\<stylesheet> and linked to the html pages as css/\<stylesheet>
 

Parameter sources have the following order of precedence: command line arguments, environment variables, config file values. This means that you can use the command line arguments to override your default values set in the config file or environment. You can override any number of values. If you have your default values configured already and just want to generate a copy of your site with a different stylesheet, you could run

```
 $ omnihost -s <stylesheet/path>
```

#### Setting Default Parameters in a Config File

On macOS and linux, the config file should be stored at `~/.config/omnihost/config`

On windows, the config file should be stored at `%APPDATA%\Local\Omnihost\config.txt`

An example config file is provided as `example_config`. Copy this file to the correct path for your operating system and update the values within to your preferred default arguments.

#### Setting Default Parameters in Environment Variables
 
The ability to configure default parameters is provided mostly to make containerization easier. Environment variable names are the same as the config file parameters and can be found in `example_config`

### Running with Docker

Pull the image

```
 $ docker pull omnihost
```

Run the image substitute the values in <> with your local paths.
```
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
```

This command mounts your local input and output paths to the container, and sets the environment variables appropriately.

This is an awful lot to type every time. The above command is provided in bash script form as `run_dockerfile_example.sh`. Download this file, rename it to `run_omnihost.sh`, and update the values in <> with your local paths. Now you just have to run:
```
./run_omnihost.sh
```
 
## Roadmap
 
This is roughly ordered by priority except for conversion of gemtext to gophermaps. That's listed first because it's the biggest piece of missing functionality, but I'm planning to shore up the html conversion before adding that in
 
 * Add ability to convert gemtext to gophermaps
 * Add automated tests
 * Add support for nested directory structures for both input and output instead of requiring all input files to be in the top level of the input directory
 * Add ability to insert header/footer on output gemtext files to support things like links back to the home page and copyright or license notices
 * Improve formatting of html output to make it nicely human-readable
 * Consider adding a preprocessing step using something like mdbook to allow for for meta control of generated pages. Would allow for things like:
   + stylesheets specified per page
   + titles that aren't dependent on the file name
   + metadata to support things like auto-generation of subject indexes for wikis
 * Add command line argument to write provided args to a config file instead of requiring the user to set that up by hand

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details
