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
from util import output_at_next_level

def print_usage():
    """
    Print correct program usage.
    """
    sys.stderr.write("""Python script which checks if the tiles at zoom level z are too large and
    splits them into the four subtiles at zoom level z+1.
    
    Usage: python3 split-initial-tiles.py TILE_SIZES_FILE MAX_NODE_COUNT
        TILES_SIZES_FILE: file which lists the number of nodes in all tiles at zoom level z
        MAX_NODE_COUNT: threshold; tiles with more nodes will be splitted.

    This script will write the IDs of the tiles to STDOUT. Use sort to sort them.

    Example: python3 dense-tiles-filter.py tile-sizes-z9.txt 5000 | sort > result-z9.txt\n""")
    exit(1)

if len(sys.argv) != 3:
    print_usage()
tile_sizes_file = open(sys.argv[1], "r")
max_node_count = int(sys.argv[2])
while True:
    line = tile_sizes_file.readline()
    if line == "\n" or line == "":
        break
    line = line.replace(" ", "/")
    elements = line.split("/")
    if len(elements) < 4:
        break
    node_count = int(elements[3])
    if node_count >= max_node_count:
        # The tile is too large.
        output_at_next_level(int(elements[1]), int(elements[2]), int(elements[0]))
    else:
        # The tile is not too large.
        sys.stdout.write(("{}/{}/{}\n".format(elements[0], elements[1], elements[2])))
