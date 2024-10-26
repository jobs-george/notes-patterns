# Getting Started

## Python

Since this is a _Python_ design pattern course, 
you'll need Python, 
specifically Python 3.
Check if Python is already installed with,

```sh
python --version
#> Python 3.10.12
```

If Python isn't installed, 
follow the installation instructions [here](https://www.python.org/).

## Pylint

The easiest way to install pylint is via the VSCode extension.
Otherwise, install from the command line with,

```sh
pip install pylint
```

and run on the example file,

```sh
pylint 00-intro/app.py
#> 00-intro/app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
#> 00-intro/app.py:3:0: R0903: Too few public methods (1/2) (too-few-public-methods)
#> 00-intro/app.py:63:13: E1120: No value for argument 'y' in constructor call (no-value-for-parameter)
```