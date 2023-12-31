#!/usr/bin/env python
#
# Copyright  2014  Nickolay V. Shmyrev
#            2016  Johns Hopkins University (author: Daniel Povey)
# Apache 2.0


from __future__ import print_function
import sys
from codecs import open

# This script joins together pairs of split-up words like "you 're" -> "you're".
# The TEDLIUM transcripts are normalized in a way that's not traditional for
# speech recognition.

for line in sys.stdin:
    items = line.split()
    new_items = []
    i = 1
    while i < len(items):
        if i < len(items) - 1 and items[i + 1][0] == "'":
            new_items.append(items[i] + items[i + 1])
            i = i + 1
        else:
            new_items.append(items[i])
        i = i + 1
    print(items[0] + " " + " ".join(new_items))
