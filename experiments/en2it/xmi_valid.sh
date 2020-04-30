#!/bin/bash

src="en"
tgt="it"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
