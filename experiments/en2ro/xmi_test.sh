#!/bin/bash

src="en"
tgt="ro"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
