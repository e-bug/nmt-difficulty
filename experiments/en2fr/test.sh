#!/bin/bash

src="en"
tgt="fr"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
