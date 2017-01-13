#! /usr/bin/env python3

# Copyright 2017 Michael Reichert
# 
# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:
# 
#     1. Redistributions of source code must retain the above copyright notice, this list of
#     conditions and the following disclaimer.
# 
#     2. Redistributions in binary form must reproduce the above copyright notice, this list of
#     conditions and the following disclaimer in the documentation and/or other materials provided
#     with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

def output_at_next_level(x, y, zoom):
    """
    Print the IDs of the four subtiles of the tile zoom/x/y.

    Parameters
    ----------
    x : int
        x index of the tile
    y : int
        y index of the tile
    zoom : int
        zoom level of the tile
    """
    # To get the x and y index of the subtile at zoom level z+1 in the north-west corner, the x and y index have to be multiplied by 2.
    # To get the x and y index of the tile at zoom level z-1 which covers this tile, the x and y index have to be multiplied by 2^(-1).
    x_northwest = x * 2
    y_northwest = y * 2
    # output all subtiles
    for x_offset in range(0, 2):
        for y_offset in range(0, 2):
            sys.stdout.write("{}/{}/{}\n".format(zoom+1, x_northwest + x_offset, y_northwest + y_offset))
    return
