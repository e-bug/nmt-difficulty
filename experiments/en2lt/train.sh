#!/bin/bash

src="en"
tgt="lt"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
