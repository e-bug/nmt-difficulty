#!/bin/bash

src="hu"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
