#!/bin/bash

src=$1
tgt=$2
DATA_PATH="$HOME/data/nmt-difficulty/europarl-v7-aligned-bin/${src}2${tgt}"
CKPT_PATH="$HOME/checkpoints/nmt-difficulty/europarl-v7-aligned/${src}2${tgt}"
mkdir -p $CKPT_PATH

NODES=$3
GPUS=$4
export CUDA_VISIBLE_DEVICES=0,1,2,3
WORLD_SIZE=$[NODES * GPUS]
MASTER=$(head -n 1 ./hosts_${1}2${2})
hosts=`cat ./hosts_${1}2${2}`
h=0
n=0

params="$DATA_PATH \
        --save-dir $CKPT_PATH \
        --arch transformer_wmt_en_de \
        --dropout 0.3 \
        --share-all-embeddings \
        --optimizer adam \
        --adam-betas (0.9,0.997) \
        --adam-eps 1e-09 \
        --clip-norm 0.0 \
        --lr-scheduler inverse_sqrt \
        --warmup-init-lr 1e-07 \
        --warmup-updates 8000 \
        --lr 0.001 \
        --min-lr 1e-09 \
        --weight-decay 0.0 \
        --criterion label_smoothed_cross_entropy \
        --label-smoothing 0.1 \
        --max-tokens 2048 \
        --max-update 20000 \
        --no-progress-bar \
        --log-format json \
        --log-interval 100 \
        --save-interval 100000 \
        --save-interval-updates 500 \
        --keep-interval-updates 100
"

cd ../../fairseq-0.6.2
for line in $hosts; do
  if [ $line = $HOSTNAME ]; then
    start_=$n
    end_=$[n + GPUS - 1]
    GPU_RANKS=`seq -s' ' $start_ $end_`
    for gpu in `seq $[GPUS - 1]`; do
      python train.py $params --distributed-world-size $WORLD_SIZE --distributed-init-method tcp://$MASTER:10000 --distributed-rank $[n + gpu - 1] --device-id $[gpu - 1] &
    done
    python train.py $params --distributed-world-size $WORLD_SIZE --distributed-init-method tcp://$MASTER:10000 --distributed-rank $[n + GPUS - 1] --device-id $[GPUS - 1]
  fi
  h=$[h + 1]
  n=$[n + GPUS]
done
