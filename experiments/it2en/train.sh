#!/bin/bash

src="it"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
