#!/bin/bash

src="pt"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
