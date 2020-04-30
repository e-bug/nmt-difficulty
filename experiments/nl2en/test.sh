#!/bin/bash

src="nl"
tgt="en"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
