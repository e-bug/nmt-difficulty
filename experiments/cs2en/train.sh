#!/bin/bash

src="cs"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
