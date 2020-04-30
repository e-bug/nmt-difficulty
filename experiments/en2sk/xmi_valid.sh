#!/bin/bash

src="en"
tgt="sk"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
