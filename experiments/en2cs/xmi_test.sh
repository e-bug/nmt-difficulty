#!/bin/bash

src="en"
tgt="cs"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
