#!/bin/bash

src="el"
tgt="en"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
