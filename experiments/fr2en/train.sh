#!/bin/bash

src="fr"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
