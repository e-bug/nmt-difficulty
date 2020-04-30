#!/bin/bash

src="en"
tgt="de"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
