#!/bin/bash

src="en"
tgt="fi"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
