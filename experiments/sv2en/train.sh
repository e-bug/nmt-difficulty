#!/bin/bash

src="sv"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
