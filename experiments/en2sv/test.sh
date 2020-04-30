#!/bin/bash

src="en"
tgt="sv"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
