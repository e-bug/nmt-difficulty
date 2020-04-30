#!/bin/bash

src="en"
tgt="es"
split="valid"

bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
