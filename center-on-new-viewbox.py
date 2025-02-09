# -*- coding: utf-8 -*-

"""Inkscape extension for center objects on a new viewport"""

# Copyright (C) 2019, 2022, 2024  Rafael Laboissière
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


class CenterOnNewViewboxEffect(inkex.Effect):
    """Effect for centering on a newly defined viewbox"""

    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument(
            "--orientation",
            dest="orientation",
            action="store",
            default="portrait",
        )
        self.arg_parser.add_argument(
            "--format",
            dest="format",
            action="store",
            default="A4",
        )

    def effect(self):
        """Effect function"""

        paper_formats = {
            "A0": (841, 1189),
            "A1": (594, 841),
            "A2": (420, 594),
            "A3": (297, 420),
            "A4": (210, 297),
            "A5": (148, 210),
            "A6": (105, 148),
            "A7": (74, 105)
        }

        width, height = paper_formats[self.options.format]
        if self.options.orientation == "landscape":
            width, height = height, width

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


effect = CenterOnNewViewboxEffect()
effect.run()
