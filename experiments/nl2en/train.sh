#!/bin/bash

src="nl"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
