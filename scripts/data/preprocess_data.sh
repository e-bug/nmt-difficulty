#!/bin/bash

inpdir="$HOME/data/europarl/europarl-v7-parallel"
outdir="$HOME/data/nmt-difficulty/europarl-v7-aligned"
mosesdir="../../tools/mosesdecoder"
bpedir="../../tools/subword-nmt"

declare -a langs=("bg" "cs" "da" "de" "el" "es" "et" "fi" "fr" "hu" 
                  "it" "lt" "lv" "nl" "pl" "pt" "ro" "sk" "sl" "sv")

mkdir -p $outdir

source activate nmt

# Align data
echo "Aligning data..."
python align_data.py --input-dir $inpdir --output-dir $outdir

# Clean and tokenize data
echo "Tokenizing and cleaning data..."
for src in "${langs[@]}"
do
  # Tokenize data
  for f in ${outdir}/*.$src-en.$src; do
    fbase=${f%.*}
    ${mosesdir}/scripts/tokenizer/tokenizer.perl -q -l $src -threads 8 < $fbase.$src > $fbase.tok.$src
    ${mosesdir}/scripts/tokenizer/tokenizer.perl -q -l en -threads 8 < $fbase.en > $fbase.tok.en
  done
  # Clean train data
  for f in ${outdir}/train.$src-en.tok.en; do
    fbase=${f%.*}
    ${mosesdir}/scripts/training/clean-corpus-n.perl $fbase $src en "${fbase}.clean" 1 80
  done
done

# Re-align training data after cleaning
echo "Filtering training data..."
python filter_data.py --data-dir $outdir

# Learn and apply BPE
echo "Learning and applying BPE..."
for src in "${langs[@]}"
do
  for merge_ops in 16000; do
      ${bpedir}/subword_nmt/learn_joint_bpe_and_vocab.py \
        --input ${outdir}/train.$src-en.tok.clean.filt.en ${outdir}/train.$src-en.tok.clean.filt.$src \
        -s $merge_ops -o ${outdir}/bpe.$src-en.${merge_ops} \
        --write-vocabulary ${outdir}/vocab.$src-en.${merge_ops}.en ${outdir}/vocab.$src-en.${merge_ops}.$src
      lang=en
      for f in ${outdir}/train.$src-en.tok.clean.filt.${lang} ${outdir}/valid.$src-en.tok.${lang} ${outdir}/test.$src-en.tok.${lang}; do
          outfile="${f%.*}.bpe.${merge_ops}.${lang}"
          ${bpedir}/subword_nmt/apply_bpe.py -c "${outdir}/bpe.$src-en.${merge_ops}" \
            --vocabulary ${outdir}/vocab.$src-en.${merge_ops}.${lang} \
            < $f > "${outfile}"
      done
      lang=$src
      for f in ${outdir}/train.$src-en.tok.clean.filt.${lang} ${outdir}/valid.$src-en.tok.${lang} ${outdir}/test.$src-en.tok.${lang}; do
          outfile="${f%.*}.bpe.${merge_ops}.${lang}"
          ${bpedir}/subword_nmt/apply_bpe.py -c "${outdir}/bpe.$src-en.${merge_ops}" \
             --vocabulary ${outdir}/vocab.$src-en.${merge_ops}.${lang} \
             < $f > "${outfile}"
      done
  done
done

conda deactivate
