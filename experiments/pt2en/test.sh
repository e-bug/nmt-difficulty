#!/bin/bash

src="pt"
tgt="en"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
