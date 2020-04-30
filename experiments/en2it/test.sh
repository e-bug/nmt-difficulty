#!/bin/bash

src="en"
tgt="it"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
