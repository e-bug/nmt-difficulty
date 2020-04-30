#!/bin/bash

src="en"
tgt="et"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
