#!/bin/bash

src="ro"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
