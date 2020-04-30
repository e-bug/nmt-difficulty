#!/bin/bash

src="en"
tgt="da"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
