#!/bin/bash

lang=$1
split=$2
export CUDA_VISIBLE_DEVICES=2
DATA_PATH="$HOME/data/nmt-difficulty/europarl-v7-aligned-bin/$lang"
CKPT_PATH="$HOME/checkpoints/nmt-difficulty/europarl-v7-aligned/$lang"
EXP_PATH="$PWD"
OUTPUT_FN=$EXP_PATH/res-${split}.txt

mkdir -p $EXP_PATH/loss $EXP_PATH/ppl $EXP_PATH/xent


source activate nmt

cd ../../fairseq-0.6.2
python eval_lm.py $DATA_PATH \
        --gen-subset $split \
        --path $CKPT_PATH/checkpoint_best.pt \
        --task language_modeling \
        --sample-break-mode eos \
        --context-window 0 \
        --batch-size 128 \
	--log2 \
        > $OUTPUT_FN

tail -1 $OUTPUT_FN | cut -d '|' -f 2 | cut -d ' ' -f 3 | cut -d ',' -f 1 > $EXP_PATH/loss/loss.$split
tail -1 $OUTPUT_FN | cut -d '|' -f 2 | cut -d ' ' -f 5 | cut -d ',' -f 1 > $EXP_PATH/ppl/ppl.$split
tail -1 $OUTPUT_FN | cut -d '|' -f 2 | cut -d ' ' -f 7 > $EXP_PATH/xent/xent.$split


rm $OUTPUT_FN

conda deactivate
