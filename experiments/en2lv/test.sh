#!/bin/bash

src="en"
tgt="lv"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
