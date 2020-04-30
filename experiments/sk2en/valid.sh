#!/bin/bash

src="sk"
tgt="en"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
