#!/bin/bash

src="en"
tgt="cs"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
