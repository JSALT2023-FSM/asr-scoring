#!/usr/bin/env python3
# Copyright    2023  Johns Hopkins University        (authors: Desh Raj)
#
# See ../../../../LICENSE for clarification regarding multiple authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This script joins together pairs of split-up words like "you 're" -> "you're".
The TEDLIUM transcripts are normalized in a way that's not traditional for
speech recognition.

See: https://github.com/kaldi-asr/kaldi/blob/master/egs/tedlium/s5_r3/local/join_suffix.py

Input is from stdin and output is to stdout.
"""

import logging
import sys
from collections import defaultdict
from pathlib import Path


def main():
    word_list = defaultdict(list)

    for line in sys.stdin:
        reco, _, start, dur, word = line.split()
        start = float(start)
        dur = float(dur)
        word_list[reco].append((start, dur, word))

    # combine words and write to stdout
    for reco, words in word_list.items():
        cur_start = words[0][0]
        cur_dur = words[0][1]
        cur_word = words[0][2]

        for start, dur, word in words[1:]:
            if word.startswith("'"):
                cur_word += word
                cur_dur += dur
            else:
                print(f"{reco} 1 {cur_start:.2f} {cur_dur:.2f} {cur_word}")
                cur_start = start
                cur_dur = dur
                cur_word = word

        # write the last word
        print(f"{reco} 1 {cur_start:.2f} {cur_dur:.2f} {cur_word}")


if __name__ == "__main__":
    formatter = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"
    logging.basicConfig(format=formatter, level=logging.INFO)

    main()
