#!/bin/bash

src="en"
tgt="fi"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
