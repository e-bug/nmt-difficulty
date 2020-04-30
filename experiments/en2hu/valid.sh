#!/bin/bash

src="en"
tgt="hu"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
