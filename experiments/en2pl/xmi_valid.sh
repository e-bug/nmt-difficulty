#!/bin/bash

src="en"
tgt="pl"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
