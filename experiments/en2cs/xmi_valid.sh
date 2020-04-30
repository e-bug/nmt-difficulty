#!/bin/bash

src="en"
tgt="cs"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
