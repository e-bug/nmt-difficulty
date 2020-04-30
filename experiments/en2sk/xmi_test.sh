#!/bin/bash

src="en"
tgt="sk"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
