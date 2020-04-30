#!/bin/bash

src="en"
tgt="nl"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
