#!/bin/bash

src="en"
tgt="fi"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
