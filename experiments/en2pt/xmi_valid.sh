#!/bin/bash

src="en"
tgt="pt"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
