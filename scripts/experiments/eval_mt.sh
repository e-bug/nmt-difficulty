#!/bin/bash

src=$1
tgt=$2
split=$3
export CUDA_VISIBLE_DEVICES=2
DATA_PATH="$HOME/data/nmt-difficulty/europarl-v7-aligned-bin/${src}2${tgt}"
CKPT_PATH="$HOME/checkpoints/nmt-difficulty/europarl-v7-aligned/${src}2${tgt}"
EXP_PATH="$PWD"
OUTPUT_FN=$EXP_PATH/res-${split}.txt
mosesdecoder="../tools/mosesdecoder"

mkdir -p $EXP_PATH/outputs $EXP_PATH/bleu $EXP_PATH/loss $EXP_PATH/ppl $EXP_PATH/xent


source activate nmt

cd ../../fairseq-0.6.2
python generate.py $DATA_PATH \
        --gen-subset $split \
        --path $CKPT_PATH/checkpoint_best.pt \
        --batch-size 128 \
        --remove-bpe \
        --beam 4 \
        --lenpen 0.6 \
        > $OUTPUT_FN

# Extract source, predictions and ground truth
grep '^S-[0-9]*' $OUTPUT_FN | sed 's|^..||' | sort -k1 -n | cut -f2 > $EXP_PATH/outputs/src.tok.$split
grep '^H-[0-9]*' $OUTPUT_FN | sed 's|^..||' | sort -k1 -n | cut -f3 > $EXP_PATH/outputs/preds.tok.$split
grep '^T-[0-9]*' $OUTPUT_FN | sed 's|^..||' | sort -k1 -n | cut -f2 > $EXP_PATH/outputs/truth.tok.$split

# Detokenize
perl $mosesdecoder/scripts/tokenizer/detokenizer.perl -q -l $tgt \
        < $EXP_PATH/outputs/preds.tok.$split \
        > $EXP_PATH/outputs/preds.detok.$split
perl $mosesdecoder/scripts/tokenizer/detokenizer.perl -q -l $tgt \
        < $EXP_PATH/outputs/truth.tok.$split \
        > $EXP_PATH/outputs/truth.detok.$split

# Fix some moses detokenization
sed "s| '|'|g" $EXP_PATH/outputs/preds.detok.$split | sed "s| /|/|g" | sed "s|/ |/|g" \
        > $EXP_PATH/outputs/preds.$split
sed "s| '|'|g" $EXP_PATH/outputs/truth.detok.$split | sed "s| /|/|g" | sed "s|/ |/|g" \
        > $EXP_PATH/outputs/truth.$split
rm $EXP_PATH/outputs/preds.detok.$split $EXP_PATH/outputs/truth.detok.$split

# Compute BLEU
cat $EXP_PATH/outputs/preds.$split \
        | sacrebleu $EXP_PATH/outputs/truth.$split \
        > $EXP_PATH/bleu/bleu.$split

# Evaluate Loss Perplexity and Cross-entropy
python eval_mt.py $DATA_PATH \
        --gen-subset $split \
        --path $CKPT_PATH/checkpoint_best.pt \
        --task translation \
        --source-lang $src \
        --target-lang $tgt \
        --batch-size 128 \
	--log2 \
        > $OUTPUT_FN

tail -1 $OUTPUT_FN | cut -d '|' -f 2 | cut -d ' ' -f 3 | cut -d ',' -f 1 > $EXP_PATH/loss/loss.$split
tail -1 $OUTPUT_FN | cut -d '|' -f 2 | cut -d ' ' -f 5 | cut -d ',' -f 1 > $EXP_PATH/ppl/ppl.$split
tail -1 $OUTPUT_FN | cut -d '|' -f 2 | cut -d ' ' -f 7 > $EXP_PATH/xent/xent.$split


rm $OUTPUT_FN

conda deactivate
