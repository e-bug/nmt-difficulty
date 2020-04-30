#!/bin/bash

src="sl"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
