#!/bin/bash

src="en"
tgt="et"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
