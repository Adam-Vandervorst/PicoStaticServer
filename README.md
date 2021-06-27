# PicoStaticServer
A Python test server for your static sites in less than twenty lines of code.

### Usage
```shell
$ python serve.py 4242 Home /StaticGen/out
```
Serves the static files in the `~/StaticGen/out` directory at http://localhost:4242/ with `Home.html` as the entry point.

- The first argument binds to the port used, with the default being `4242`.
- The second argument determines what file to serve at `/`, defaults to `index.html`.
- The third argument specifies the directory to serve files from, uses the current working directory if left unspecified.

You can safely terminate the program with `CTRL+C`.

### Context
This script is meant as a copy-paste utility for trying out your static sites.
You likely don't want to use this; it is only tested on the two projects for which I wrote it. Moreover, the built-in alternative allows you to specify a directory to serve as of version 3.7. You can use the built-in server as follows:
```shell
$ python -m http.server 4242 -d /StaticGen/out
```
I have another 'pico' repository, [PicoVector](https://github.com/Adam-Vandervorst/PicoVector), which provides a minimal but elegant vector class for a few languages.

**Fun fact:**
The source code is the smallest file in this repository.
