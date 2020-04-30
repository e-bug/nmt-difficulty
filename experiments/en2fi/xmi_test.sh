#!/bin/bash

src="en"
tgt="fi"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
