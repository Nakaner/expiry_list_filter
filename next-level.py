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

def read_nextfile_line(tile_sizes_file_next, x, y, max_node_count):
    while True:
        # remember the position of the file pointer before reading the next line
        position_before_readline = tile_sizes_file_next.tell()
        line_next = tile_sizes_file_next.readline()
        if line_next == "":
            # end of file reached
            return True
        # remove whitespace, split node count and tile ID
        line_parts = line_next.strip().split(" ")
        line_next = line_next.replace(" ", "/")
        elements = line_parts[0].split("/")
        if elements[1] == x and elements[2] == y:
            if int(line_parts[1]) >= max_node_count:
                output_at_next_level(int(elements[1]), int(elements[2]), next_zoom)
            else:
                sys.stdout.write("{}/{}/{}\n".format(next_zoom, elements[1], elements[2]))
            return False
        # Check if the tile we look for is not listed in the nextfile.
        elif line_parts[0] > "{}/{}/{}".format(elements[0], x, y):
            sys.stdout.write("{}/{}/{}\n".format(next_zoom, x, y))
            # Jump back to the position of the file pointer before reading this line because the file is sorted alphabetically
            tile_sizes_file_next.seek(position_before_readline, 0)
            return False

def print_usage():
    """
    Print correct program usage.
    """
    sys.stderr.write("""Usage: python3 dense-tiles-filter-next.py TILE_SIZES_ZOOM_THIS TILE_SIZES_FILE_ZOOM_NEXT NEXT_LEVEL MAX_NODE_COUNT

    This will write the IDs of the tiles to STDOUT. Use sort to sort them.

    Example: python3 dense-tiles-filter.py result-z9.txt sizes-z10.txt 10 5000 | sort > result-z10.txt\n""")
    exit(1)

if len(sys.argv) != 5:
    print_usage()
tile_sizes_file_this = open(sys.argv[1], "r")
tile_sizes_file_next = open(sys.argv[2], "r")
next_zoom = int(sys.argv[3])
max_node_count = int(sys.argv[4])
next_finished = False
while True:
    line = tile_sizes_file_this.readline()
    if line == "":
        # We reached the end of the file.
        break
    elements = line.strip().split("/")
    if len(elements) < 3:
        # Empty or invalid lines are not allowed.
        sys.stderr.write("ERROR: Invalid Syntax:\n{}".format(line))
        break
    zoom = int(elements[0])
    if zoom == next_zoom:
        if next_finished:
            continue
        # check size of this tile
        next_finished = read_nextfile_line(tile_sizes_file_next, elements[1], elements[2], max_node_count)
    else:
        sys.stdout.write(line)
