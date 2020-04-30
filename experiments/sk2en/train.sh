#!/bin/bash

src="sk"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
