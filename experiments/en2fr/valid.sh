#!/bin/bash

src="en"
tgt="fr"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
