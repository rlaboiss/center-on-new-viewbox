# -*- coding: utf-8 -*-

"""Inkscape extension for setting the viewport to a centered A4 sheet"""

# Copyright (C) 2019, 2022  Rafael Laboissière
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# The complete text of the GNU General Public License can be obtained at
# http://www.gnu.org/licenses/.

import sys

sys.path.append("/usr/share/inkscape/extensions")
import inkex  # noqa


class SetA4ViewportEffect(inkex.Effect):
    """Effect for setting the Viewport to A4 paper format"""

    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument(
            "--orientation",
            dest="orientation",
            action="store",
            default="portrait",
        )

    def effect(self):
        """Effect function"""

        # Set the width and height of an A4 paper, according to the
        # orientation (portrait or landscape)
        if self.options.orientation == "portrait":
            width = 210
            height = 297
        else:
            width = 297
            height = 210

        if self.svg.selected:
            # Get the bounding box of the selected objects
            bbox = self.svg.selected.bounding_box()
            vbox = [bbox.left, bbox.top, bbox.width, bbox.height]
        else:
            # Get the current page dimensions if there is no selection
            root = self.svg.getElement("//svg:svg")
            vbox = [float(i) for i in root.get("viewBox").split(" ")]

        # Compute the new position of the viewBox
        posx = vbox[0] - (width - vbox[2]) / 2
        posy = vbox[1] - (height - vbox[3]) / 2
        root = self.svg.getElement("//svg:svg")
        root.set("viewBox", f"{posx} {posy} {width} {height}")
        root.set("width", f"{width}mm")
        root.set("height", f"{height}mm")


effect = SetA4ViewportEffect()
effect.run()
