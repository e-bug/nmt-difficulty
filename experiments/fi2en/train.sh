#!/bin/bash

src="fi"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
