pydoc-quarto
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` sh
pip install pydoc_quarto
```

## Usage

``` python
!pydoc_quarto -h
```

    usage: pydoc_quarto [-h] lib dest_dir

    Generate Quarto Markdown API docs

    positional arguments:
      lib         the name of the python library
      dest_dir    the destination directory the markdown files will be rendered into

    options:
      -h, --help  show this help message and exit

## Example

This will generate markdown files for the `requests` library:

``` python
!pydoc_quarto requests _test_dir/
!ls _test_dir/
```

    adapters.qmd     compat.qmd       hooks.qmd        status_codes.qmd
    api.qmd          cookies.qmd      models.qmd       structures.qmd
    auth.qmd         exceptions.qmd   packages.qmd     utils.qmd
    certs.qmd        help.qmd         sessions.qmd
