#!/bin/bash

src="en"
tgt="lt"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
