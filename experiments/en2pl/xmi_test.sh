#!/bin/bash

src="en"
tgt="pl"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
