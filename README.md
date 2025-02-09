# Center on new viewbox

## Description

This Inkscape extension sets the viewbox to a ISO 216 paper format (either
portrait or landscape) and center the content of the selected drawing to
that viewbox. This may be useful for printing the drawing and ensuring
that it will be centered on the paper.

## Installation

Copy the files `center-on-new-viewbox.inx` and `center-on-new-viewbos.py`
into the Inkscape's `extensions/` directory. In Linux systems, you can use
the provided `Makefile` to install the files into the user's extensions
directory, by running:

```sh
$ make install
```

It is also possible to install directly from the Git repository. Change to
the `extensions` directory (in Linux systems either the system-wide
`/usr/share/inkscape/extensions` or the user-specfic
`~/.config/inkscape/extensions/`) and run, in a terminal:

```sh
git clone https://github.com/rlaboiss/center-on-new-viewbox.git
```

## Usage

Select the menu item Extensions → Document → Center on new viewbox. Either
portrait or landscape orientation can be chosen. Several paper format are
proposed (friom A0 to A7). The current viewbox will be resized to the
dimensions of the chosen paper format. The previous page is centered on the
new viewbox.

If there is an object or group of objects selected, then it will be
centered in the new viewbox.

## Author

Copyright (C) 2019, 2022, 2025 Rafael Laboissière (<rafael@laboissiere.net>)

Released under the GNU General Public License, version 3 or later. No warranties.
