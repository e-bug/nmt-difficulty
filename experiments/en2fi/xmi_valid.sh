#!/bin/bash

src="en"
tgt="fi"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
