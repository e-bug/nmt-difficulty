#!/bin/bash

src="en"
tgt="lt"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
