#!/bin/bash

src="en"
tgt="el"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
