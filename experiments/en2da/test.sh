#!/bin/bash

src="en"
tgt="da"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
