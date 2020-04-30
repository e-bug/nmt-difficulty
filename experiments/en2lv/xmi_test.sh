#!/bin/bash

src="en"
tgt="lv"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
