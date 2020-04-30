#!/bin/bash

src="en"
tgt="fr"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
