#!/bin/bash

src="en"
tgt="de"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
