#!/bin/bash

src="en"
tgt="bg"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
