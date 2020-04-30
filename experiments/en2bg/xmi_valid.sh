#!/bin/bash

src="en"
tgt="bg"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
