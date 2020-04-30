#!/bin/bash

src="bg"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
