#!/bin/bash

src="en"
tgt="bg"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
