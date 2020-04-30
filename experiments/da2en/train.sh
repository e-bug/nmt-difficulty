#!/bin/bash

src="da"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
