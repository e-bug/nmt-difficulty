#!/bin/bash

src="en"
tgt="de"
split="test"

bash ../../scripts/experiments/compute_xmi.sh $src $tgt $split
