#!/bin/bash

src="en"
tgt="es"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
