#!/bin/bash

src="pl"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
