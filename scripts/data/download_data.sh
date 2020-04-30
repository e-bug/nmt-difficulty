#!/bin/bash

baseurl="http://www.statmt.org/europarl/v7"
datadir="$HOME/data/europarl/europarl-v7-parallel"
declare -a langs=("bg" "cs" "da" "de" "el" "es" "et" "fi" "fr" "hu" 
                  "it" "lt" "lv" "nl" "pl" "pt" "ro" "sk" "sl" "sv")

mkdir -p $datadir

echo "Downloading Europarl v7"
for src in "${langs[@]}"
do
  echo "$src-en"
  wget "$baseurl/$src-en.tgz" -O "$datadir/$src-en.tgz"
  tar -xvzf "$datadir/$src-en.tgz" -C "$datadir"
  rm "$datadir/$src-en.tgz"
done
