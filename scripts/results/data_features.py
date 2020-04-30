#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
from scipy import stats
import pandas as pd
import os.path

data_dir = '/home/user/data/nmt-difficulty/europarl-v7-aligned'

def data_feature_vec(sources, targets, 
                     dataset_template=os.path.join(data_dir, 'train.%s-%s.tok.clean.filt.%s')): 
    """
    Adapted from langrank [https://github.com/neulab/langrank/blob/master/langrank.py]
    """
    data_features = defaultdict(list)
    
    for src, tgt in zip(sources, targets):
        features = {}

        dataset_source = dataset_template % (src, tgt, src)
        try:
            with open(dataset_source) as inp:
                source_lines = inp.readlines()
        except:
            dataset_source = dataset_template % (tgt, src, src)
            with open(dataset_source) as inp:
                source_lines = inp.readlines()
        features["src_dataset_size"] = len(source_lines)
        tokens = [w for s in source_lines for w in s.strip().split()]
        features["src_token_number"] = len(tokens)
        types = set(tokens)
        features["src_type_number"] = len(types)
        features["src_word_vocab"] = types
        features["src_type_token_ratio"] = features["src_type_number"]/float(features["src_token_number"])

        dataset_target = dataset_template % (src, tgt, tgt)
        try:
            with open(dataset_target) as inp:
                source_lines = inp.readlines()
        except:
            dataset_target = dataset_template % (tgt, src, tgt)
            with open(dataset_target) as inp:
                source_lines = inp.readlines()
        features["tgt_dataset_size"] = len(source_lines)
        tokens = [w for s in source_lines for w in s.strip().split()]
        features["tgt_token_number"] = len(tokens)
        types = set(tokens)
        features["tgt_type_number"] = len(types)
        features["tgt_word_vocab"] = types
        features["tgt_type_token_ratio"] = features["tgt_type_number"]/float(features["tgt_token_number"])

        # Features
        src_token_number = features["src_token_number"]
        tgt_token_number = features["tgt_token_number"]
        rat_token_number = float(src_token_number / tgt_token_number)

        src_ttr = features["src_type_token_ratio"]
        tgt_ttr = features["tgt_type_token_ratio"]
        distance_ttr = (1 - float(src_ttr) / tgt_ttr) ** 2

        word_overlap = float(len(set(features["src_word_vocab"]).intersection(set(features["tgt_word_vocab"])))) / (features["src_type_number"] + features["tgt_type_number"])

        data_specific_feats = {n: v for n, v in zip(['rat_token_number', 'src_ttr', 'tgt_ttr', 'distance_ttr', 'word_overlap'],
                                                    [rat_token_number, src_ttr, tgt_ttr, distance_ttr, word_overlap])}

        for n, v in data_specific_feats.items():
            data_features[n].append(v)
    
    return data_features


langs = ["bg", "cs", "da", "de", "el", "es", "et", "fi", "fr", "hu", 
         "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv"]
xmi = pd.read_csv("../../results/test/xmi.mt.csv").set_index(["src", "tgt"])
pair2xmi = xmi.to_dict()['value']

print('Into En')
data_feats_into = data_feature_vec(langs, ['en']*len(langs))
print('Distance\t Pearson\t\t Spearman')
for k, v in data_feats_into.items():
    losses = []
    distances = []
    for ix, l in enumerate(langs):
        losses.append(pair2xmi[(l, 'en')])
        distances.append(v[ix])
    pearsonr, pearsonp = stats.pearsonr(losses, distances)
    spearmanr, spearmanp = stats.spearmanr(losses, distances)
    print(k, '\t', '%.4f' % pearsonr, '(%.4f)'% pearsonp, '\t', '%.4f' % spearmanr, '(%.4f)' % spearmanp)

print('From En')
data_feats_from = data_feature_vec(['en']*len(langs), langs)
print('Distance\t Pearson\t\t Spearman')
for k, v in data_feats_from.items():
    losses = []
    distances = []
    for ix, l in enumerate(langs):
        losses.append(pair2xmi[('en', l)])
        distances.append(v[ix])
    pearsonr, pearsonp = stats.pearsonr(losses, distances)
    spearmanr, spearmanp = stats.spearmanr(losses, distances)
    print(k, '\t', '%.4f' % pearsonr, '(%.4f)'% pearsonp, '\t', '%.4f' % spearmanr, '(%.4f)' % spearmanp)

print('Both')
print('Distance\t Pearson\t\t Spearman')
for k, v in data_feats_into.items():
    losses = []
    distances = []
    for ix, l in enumerate(langs):
        losses.append(pair2xmi[(l, 'en')])
        distances.append(v[ix])
    for ix, l in enumerate(langs):
        losses.append(pair2xmi[('en', l)])
        distances.append(data_feats_from[k][ix])
    pearsonr, pearsonp = stats.pearsonr(losses, distances)
    spearmanr, spearmanp = stats.spearmanr(losses, distances)
    print(k, '\t', '%.4f' % pearsonr, '(%.4f)'% pearsonp, '\t', '%.4f' % spearmanr, '(%.4f)' % spearmanp)


# Saving features
for k, v in data_feats_into.items():
    with open('../../results/features/%s.csv' % k, 'w') as f:
        f.write('src,tgt,value\n')
        for ix, l in enumerate(langs):
            f.write(l + ',en,%f\n' % v[ix])
        for ix, l in enumerate(langs):
            f.write('en,%s,%f\n' % (l, data_feats_from[k][ix]))

