#!/bin/bash

src="en"
tgt="sv"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
