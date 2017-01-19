Expiry List Filer
=================

Expiry list filter is a collection of tools to split up the world (OSM planet data)
into small chunks which can be processed separately.


The components
==============

dense_tiles
-----------

dense_tiles is a utility by Frederik Ramm which is part of the
[osmium-contrib](https://github.com/osmcode/osmium-contrib/tree/master/dense_tiles) collection.
It calculates on a given zoom level which tiles are the
largest tiles by the number of nodes in them and outputs the number of nodes of each tile.
I suggest to use [my fork](https://github.com/Nakaner/osmium-contrib/tree/dense_tiles_more_options/dense_tiles) which adds two more command line arguments.

split-initial-tiles.py
----------------------

This Python3 script reads the alphabetically(!) sorted (use `sort`) output of dense_tiles
and splits up all tiles which contain more than n nodes. It's your choice which threshold
you choose. I suggest 5000.


next-level.py
-------------

The second step has to be repeated in a similar manner, but now you use next-level.py.


The steps in simple words
=========================

Assumptions in the following steps:

* minimal zoom level: 9
* maximum zoom level: 15
* node count threshold: 5000

1. Run `./dense_tiles -sac -z 9 PLANETFILE | sort > tile-sizes-z9.txt`.
`PLANETFILE` is the planet file. This step will take about 15 minutes.
2. Repeat for every zoom level from 10 to 15:
`./dense_tiles -sac -M 5000 -z ZOOM_LEVEL PLANETFILE | sort tile-sizes-zZOOM_LEVEL.txt`.
3. Run `python3 split-inital-tiles.py tile-sizes-z9.txt 5000 | sort > z9.txt`
4. Repeat for each zoom level from 10 to 15:
`python3 next-level.py zZOOM_THIS.txt tile-sizes-zZOOM_NEXT.txt ZOOM_NEXT 5000 | sort > zZOOM_NEXT.txt`

License
=======

Copyright (c) 2017, Michael Reichert
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

