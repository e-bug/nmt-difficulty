#!/bin/bash

src="en"
tgt="es"
split="test"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
