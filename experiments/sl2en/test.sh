#!/bin/bash

src="sl"
tgt="en"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
