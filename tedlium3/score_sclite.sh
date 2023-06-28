#!/usr/bin/env bash
set -euo pipefail

# How to use:
# Create a working directory containing `dev` and `test` sub-directories, and copy
# your output CTM files there (named hyp.ctm). Then run this script from the
# root tedlium3 directory.

# NOTE: TEDLium3 transcripts separate out suffixes such as they're -> they 're.
# We join them together for scoring (see below `join_suffix_stm.py`). We do the same
# for the CTM files. This should make no difference if you are already producing words
# where suffixes are combined.

# Add sclite to PATH
export PATH=$PATH:../sctk/bin

exp_dir=exp/

log() {
  # This function is from espnet
  local fname=${BASH_SOURCE[1]##*/}
  echo -e "$(date '+%Y-%m-%d %H:%M:%S') (${fname}:${BASH_LINENO[0]}:${FUNCNAME[1]}) $*"
}

log "Computing WERs using sclite"
for part in dev test; do
  scoring_dir=$exp_dir/$part
  cat $scoring_dir/hyp.ctm | python local/join_suffix_ctm.py > $scoring_dir/hyp_score.ctm
  cat assets/legacy_stm/$part/*.stm | python local/join_suffix_stm.py > $scoring_dir/ref.stm
  sclite -r $scoring_dir/ref.stm stm -h $scoring_dir/hyp_score.ctm ctm \
    -O $scoring_dir -o all
  log "Scoring reports are written to $scoring_dir/hyp_score.ctm.sys"
done