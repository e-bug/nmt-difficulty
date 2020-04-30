#!/bin/bash

src="et"
tgt="en"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
