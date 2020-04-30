#!/bin/bash

src="en"
tgt="pt"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
