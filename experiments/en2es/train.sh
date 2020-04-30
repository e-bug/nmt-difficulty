#!/bin/bash

src="en"
tgt="es"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
