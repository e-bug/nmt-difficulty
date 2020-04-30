#!/bin/bash

src="en"
tgt="nl"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
