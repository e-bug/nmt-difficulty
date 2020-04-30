#!/bin/bash

src="nl"
tgt="en"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
