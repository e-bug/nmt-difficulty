#!/bin/bash

src="da"
tgt="en"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
