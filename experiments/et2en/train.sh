#!/bin/bash

src="et"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
