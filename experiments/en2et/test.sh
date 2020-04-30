#!/bin/bash

src="en"
tgt="et"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
