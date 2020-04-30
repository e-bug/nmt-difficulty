#!/bin/bash

src="en"
tgt="fr"
split="valid"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
