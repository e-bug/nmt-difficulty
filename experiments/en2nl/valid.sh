#!/bin/bash

src="en"
tgt="nl"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
