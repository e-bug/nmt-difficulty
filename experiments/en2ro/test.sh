#!/bin/bash

src="en"
tgt="ro"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
