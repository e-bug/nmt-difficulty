#!/bin/bash

src="it"
tgt="en"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
