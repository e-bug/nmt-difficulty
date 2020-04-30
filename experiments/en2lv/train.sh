#!/bin/bash

src="en"
tgt="lv"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
