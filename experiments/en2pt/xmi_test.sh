#!/bin/bash

src="en"
tgt="pt"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
