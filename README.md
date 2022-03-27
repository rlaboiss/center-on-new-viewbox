# Set centered A4 viewport

## Description

This Inkscape extension sets the viewport to the A4 format (either portrait
or landscape) and center the content of the drawing to that viewport. This
may be useful for printing the drawing and ensuring that it will be centered
on the paper.

## Installation

Copy the files `set-a4-viewport.inx` and `set-a4-viewport.py` into the
Inkscape's `extensions/` directory. In Linux systems, you can use the
provided `Makefile` to install the files into the user's extensions
directory, by running:

```sh
$ make install
```

## Usage

Just select the menu item Extensions → Document → Set A4 viewport. Either
portrait or landscape orientation can be chosen.

## Limitations

This extension is limited to the A4 format. It will be eventually improved
in order to allow other paper formats.

## Author

Copyright (C) 2019, 2022 Rafael Laboissière (<rafael@laboissiere.net>)

Released under the GNU General Public License, version 3 or later. No warranties.
