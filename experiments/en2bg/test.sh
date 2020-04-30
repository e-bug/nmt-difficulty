#!/bin/bash

src="en"
tgt="bg"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
