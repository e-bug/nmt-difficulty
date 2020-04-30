#!/bin/bash

src="en"
tgt="sk"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
