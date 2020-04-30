#!/bin/bash

src="en"
tgt="sv"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
