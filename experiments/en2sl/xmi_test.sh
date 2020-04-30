#!/bin/bash

src="en"
tgt="sl"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
