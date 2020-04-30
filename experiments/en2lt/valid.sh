#!/bin/bash

src="en"
tgt="lt"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
