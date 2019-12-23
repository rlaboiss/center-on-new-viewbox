# Set centered A4 viewport

## Description

This Inkscape extension sets the viewport to the A4 portrait format and
center the content of the drawing to that viewport.  This may be useful for
printing the drawing and ensuring that it will centered on the paper.

## Installation

Copy the files `set-a4-viewport.inx` and `set-a4-viewport.py` the
Inkscape's `extensions/` directory.  In Linux systems, you can use the
provided `Makefile` to install te file in the user's extensions directory:

```sh
$ make install
```

## Usage

Just select the menu item Document → Set A4 viewport.

## Limitations

This extension is limited to the A$ format in the ortrait orientation.  It
will be eventually improved to allow other paper formats and the landscape
orientation.

## Author

Copyright (C) 2019  Rafael Laboissière (<rafael@laboissiere.net>)

Released under the GNU General Public License, version 3 or later.  No warranties.
