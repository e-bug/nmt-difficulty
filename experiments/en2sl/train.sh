#!/bin/bash

src="en"
tgt="sl"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
