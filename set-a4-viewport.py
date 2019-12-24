# -*- coding: utf-8 -*-
# Inkscape extension for setting the viewport to a centered A4 portrait sheet
# Copyright (C) 2019  Rafael Laboissière
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
sys.path.append ('/usr/share/inkscape/extensions')
import inkex
from subprocess import Popen, PIPE

class SetA4ViewportEffect (inkex.Effect):
    def __init__ (self):
        inkex.Effect.__init__ (self)
        self.OptionParser.add_option ('--orientation', dest = 'orientation',
                                      action = 'store', type = 'string',
                                      default = 'portrait')

    def effect(self):
        dpi = 96
        scale = dpi / 25.4
        if self.options.orientation == 'portrait':
            width_mm = 210
            height_mm = 297
        else:
            width_mm = 297
            height_mm = 210
        width_px = width_mm * scale
        height_px = height_mm * scale
        root = self.xpathSingle ('//svg:svg')
        vb = [float (i) for i in root.get ('viewBox').split (' ')]
        command = ('inkscape --without-gui --query-all "{}"'
                   .format (self.svg_file))
        p = Popen (command, shell = True, stdout = PIPE, stderr = PIPE)
        rc = p.wait ()
        s = p.stdout.readline ()
        bbox = [float (i) for i in s.split (',') [1 : 5]]
        x = vb [0] + bbox [0] - (width_px - bbox [2]) / 2
        y = vb [1] + bbox [1] - (height_px - bbox [3]) / 2
        root = self.xpathSingle ('//svg:svg')
        root.set ('viewBox', '{} {} {} {}'.format (x, y, width_px, height_px))
        root.set ('width', '{}mm'.format (width_mm))
        root.set ('height', '{}mm'.format (height_mm))

effect = SetA4ViewportEffect ()
effect.affect ()
