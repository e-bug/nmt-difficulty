#!/bin/bash

src="en"
tgt="pl"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
