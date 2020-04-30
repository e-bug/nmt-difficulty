#!/bin/bash

src="en"
tgt="lv"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
