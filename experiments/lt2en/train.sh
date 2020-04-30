#!/bin/bash

src="lt"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
