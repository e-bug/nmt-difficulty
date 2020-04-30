#!/bin/bash

src="en"
tgt="sl"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
