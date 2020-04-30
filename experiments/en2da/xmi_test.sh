#!/bin/bash

src="en"
tgt="da"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
