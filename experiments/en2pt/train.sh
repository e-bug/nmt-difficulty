#!/bin/bash

src="en"
tgt="pt"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
