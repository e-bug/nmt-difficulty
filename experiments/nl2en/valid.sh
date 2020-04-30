#!/bin/bash

src="nl"
tgt="en"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
