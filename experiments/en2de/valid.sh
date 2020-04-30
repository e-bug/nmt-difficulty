#!/bin/bash

src="en"
tgt="de"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
