#!/bin/bash

src="en"
tgt="et"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
