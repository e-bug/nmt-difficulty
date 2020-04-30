#!/bin/bash

src="sk"
tgt="en"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
