#!/bin/bash

src="en"
tgt="el"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
