#!/bin/bash

src="en"
tgt="sv"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
