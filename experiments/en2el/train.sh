#!/bin/bash

src="en"
tgt="el"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
