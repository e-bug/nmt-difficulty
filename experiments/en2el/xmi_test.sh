#!/bin/bash

src="en"
tgt="el"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
