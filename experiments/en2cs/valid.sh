#!/bin/bash

src="en"
tgt="cs"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
