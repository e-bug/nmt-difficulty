#!/bin/bash

src="en"
tgt="el"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
