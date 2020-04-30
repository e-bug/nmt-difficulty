#!/bin/bash

src="de"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
