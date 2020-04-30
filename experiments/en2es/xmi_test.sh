#!/bin/bash

src="en"
tgt="es"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
