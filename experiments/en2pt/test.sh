#!/bin/bash

src="en"
tgt="pt"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
