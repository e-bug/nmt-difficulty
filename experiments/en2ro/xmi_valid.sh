#!/bin/bash

src="en"
tgt="ro"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
