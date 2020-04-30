#!/bin/bash

src="en"
tgt="sv"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
