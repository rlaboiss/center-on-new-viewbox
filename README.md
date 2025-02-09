# Center on new viewport

## Description

This Inkscape extension sets the viewport to a ISO 216 paper format (either
portrait or landscape) and center the content of the selected drawing to
that viewport. This may be useful for printing the drawing and ensuring
that it will be centered on the paper.

Notice that the name of this extension “set-a4-viewport” comes from a
legacy state, when the viewport format was restricted to A4 paper format.

## Installation

Copy the files `set-a4-viewport.inx` and `set-a4-viewport.py` into the
Inkscape's `extensions/` directory. In Linux systems, you can use the
provided `Makefile` to install the files into the user's extensions
directory, by running:

```sh
$ make install
```

It is also possible to install directly from the Git repository. Change to
the `extensions` directory (in Linux systems either the system-wide
`/usr/share/inkscape/extensions` or the user-specfic
`~/.config/inkscape/extensions/`) and run, in a terminal:

```sh
git clone https://github.com/rlaboiss/set-a4-viewport.git
```

## Usage

Select the menu item Extensions → Document → Center on new viewport. Either
portrait or landscape orientation can be chosen. Several paper format are
proposed (friom A0 to A7). The current viewport will be resized to the
dimensions of the chosen paper format. The previous page is centered on the
new viewport.

If there is an object or group of objects selected, then it will be
centered in the new viewport.

## Author

Copyright (C) 2019, 2022, 2025 Rafael Laboissière (<rafael@laboissiere.net>)

Released under the GNU General Public License, version 3 or later. No warranties.
