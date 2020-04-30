#!/bin/bash

src="es"
tgt="en"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
