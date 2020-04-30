#!/bin/bash

src="en"
tgt="pl"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
