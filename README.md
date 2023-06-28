# JSALT ASR scoring

This repository is a collection of scripts and tools for scoring ASR output for the
common datsets being using in JSALT 2023 FST team.

## Supported scoring tools

- [x] sclite
- [x] kaldialign
- [ ] fstalign

### Adding a new scoring tool

1. Create an installation script for the tool.
2. Create an example scoring script in one of the dataset directories.

## Supported datasets

- [x] TEDLium-3
- [ ] Librispeech
- [ ] VoxPopuli

1. Create a directory for the dataset.
2. Create an `assets` directory to add the references (ideally in STM format).
3. Create example scoring scripts to score outputs (in CTM format).

For details about CTM and STM formats, see Section 7 in 
[this document](https://www.nist.gov/system/files/documents/2021/08/03/OpenASR20_EvalPlan_v1_5.pdf).

## Installation

```
install_sctk.sh
install_kaldialign.sh # optional
```

## Usage

```
cd tedlium3
mkdir exp/{dev,test}
cp /path/to/dev/hyp/ctm exp/dev/hyp.ctm
cp /path/to/test/ref/ctm exp/test/hyp.ctm
./score_sclite.sh
```

## Issues

Please report any issues using the issue tracker, or contact Desh Raj (r.desh26@gmail.com).