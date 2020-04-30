#!/bin/bash

src="en"
tgt="hu"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
