#!/bin/bash

src="en"
tgt="it"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
