#!/bin/bash

src="en"
tgt="hu"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
