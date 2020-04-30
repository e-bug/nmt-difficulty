#!/bin/bash

src="en"
tgt="sl"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
