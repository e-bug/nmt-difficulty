#!/bin/bash

src="en"
tgt="de"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
