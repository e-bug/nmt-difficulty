#!/bin/bash

src="en"
tgt="nl"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
