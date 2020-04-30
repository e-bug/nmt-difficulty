#!/bin/bash

src="en"
tgt="pl"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
