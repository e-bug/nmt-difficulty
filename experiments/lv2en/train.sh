#!/bin/bash

src="lv"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
