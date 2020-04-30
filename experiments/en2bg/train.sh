#!/bin/bash

src="en"
tgt="bg"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
