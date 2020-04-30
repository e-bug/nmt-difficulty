#!/bin/bash

src="en"
tgt="sk"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
