#!/bin/bash

src="en"
tgt="ro"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
