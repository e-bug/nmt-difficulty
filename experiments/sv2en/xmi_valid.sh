#!/bin/bash

src="sv"
tgt="en"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
