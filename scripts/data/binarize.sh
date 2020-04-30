#!/bin/bash

inpdir="$HOME/data/nmt-difficulty/europarl-v7-aligned"
outdir="$HOME/data/nmt-difficulty/europarl-v7-aligned-bin"

declare -a langs=("bg" "cs" "da" "de" "el" "es" "et" "fi" "fr" "hu" 
                  "it" "lt" "lv" "nl" "pl" "pt" "ro" "sk" "sl" "sv")

mkdir -p $outdir


source activate nmt

cd ../../fairseq-0.6.2
tgt="en"
for src in "${langs[@]}"
do
  # src -> en
  python preprocess.py \
        --source-lang $src \
        --target-lang $tgt \
        --trainpref $inpdir/train.$src-$tgt.tok.clean.filt.bpe.16000 \
        --validpref $inpdir/valid.$src-$tgt.tok.bpe.16000 \
        --testpref $inpdir/test.$src-$tgt.tok.bpe.16000 \
        --destdir $outdir/${src}2${tgt} \
        --workers 16 \
        --joined-dictionary
  # en -> src
  python preprocess.py \
        --source-lang $tgt \
        --target-lang $src \
	--srcdict $outdir/${src}2${tgt}/dict.$tgt.txt \
	--tgtdict $outdir/${src}2${tgt}/dict.$src.txt \
        --trainpref $inpdir/train.$src-$tgt.tok.clean.filt.bpe.16000 \
        --validpref $inpdir/valid.$src-$tgt.tok.bpe.16000 \
        --testpref $inpdir/test.$src-$tgt.tok.bpe.16000 \
        --destdir $outdir/${tgt}2${src} \
        --workers 16
  # src (lm)
  python preprocess.py \
        --trainpref $inpdir/train.$src-$tgt.tok.clean.filt.bpe.16000.$src \
        --validpref $inpdir/valid.$src-$tgt.tok.bpe.16000.$src \
        --testpref $inpdir/test.$src-$tgt.tok.bpe.16000.$src \
        --destdir $outdir/$src \
        --workers 16 \
        --only-source
done
# en (lm)
python preprocess.py \
        --trainpref $inpdir/train.bg-en.tok.clean.filt.bpe.16000.en \
        --validpref $inpdir/valid.bg-en.tok.bpe.16000.en \
        --testpref $inpdir/test.bg-en.tok.bpe.16000.en \
        --destdir $outdir/en \
        --workers 16 \
        --only-source

conda deactivate
