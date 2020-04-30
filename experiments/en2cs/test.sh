#!/bin/bash

src="en"
tgt="cs"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
