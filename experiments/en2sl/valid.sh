#!/bin/bash

src="en"
tgt="sl"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
