#!/bin/bash

src=$1
tgt=$2
split=$3
MT_PATH="$PWD"
LM_PATH="../${tgt}"

mkdir -p $MT_PATH/xmi


lm_xent="$LM_PATH/xent/xent.$split"
if [ ! -f "$lm_xent" ]; then
    echo "$lm_xent does not exist. Evaluating LM..."
    cd $LM_PATH
    bash ../../scripts/experiments/eval_lm.sh $tgt $split
    cd $MT_PATH
fi

mt_xent="$MT_PATH/xent/xent.$split"
if [ ! -f "$mt_xent" ]; then
    echo "$mt_xent does not exist. Evaluating MT..."
    bash ../../scripts/experiments/eval_mt.sh $src $tgt $split
fi


lm_xent=`cat $LM_PATH/xent/xent.$split`
mt_xent=`cat $MT_PATH/xent/xent.$split`
echo "$lm_xent - $mt_xent" | bc > $MT_PATH/xmi/xmi.$split
