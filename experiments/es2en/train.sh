#!/bin/bash

src="es"
tgt="en"

qsub ../../scripts/experiments/train_mt.cluster $src $tgt
