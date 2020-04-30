#!/bin/bash

src="en"
tgt="da"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
