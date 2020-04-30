#!/bin/bash

src="en"
tgt="hu"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
