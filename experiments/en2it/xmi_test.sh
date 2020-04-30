#!/bin/bash

src="en"
tgt="it"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
