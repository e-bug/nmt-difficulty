#!/bin/bash

src="en"
tgt="it"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
