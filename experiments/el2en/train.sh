#!/bin/bash

src="el"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
