#!/bin/bash

src="en"
tgt="ro"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
