#!/bin/bash

src="en"
tgt="fr"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
