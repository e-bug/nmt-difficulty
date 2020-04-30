#!/bin/bash

src="en"
tgt="lv"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
