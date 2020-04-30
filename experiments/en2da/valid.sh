#!/bin/bash

src="en"
tgt="da"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
