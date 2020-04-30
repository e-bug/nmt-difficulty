#!/bin/bash

src="en"
tgt="sk"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
