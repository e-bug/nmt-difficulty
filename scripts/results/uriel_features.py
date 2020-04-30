#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lang2vec.lang2vec as l2v
from scipy import stats
import pandas as pd
import iso639

def uriel_distance_vec(languages):
    """
    Adapted from langrank [https://github.com/neulab/langrank/blob/master/langrank.py]
    """
    geographic = l2v.geographic_distance(languages)
    genetic = l2v.genetic_distance(languages)
    inventory = l2v.inventory_distance(languages)
    syntactic = l2v.syntactic_distance(languages)
    phonological = l2v.phonological_distance(languages)
    featural = l2v.featural_distance(languages)
    uriel_features = {n:v for n, v in zip(['genetic', 'syntactic', 'featural', 'phonological', 'inventory', 'geographic'], 
                                          [genetic, syntactic, featural, phonological, inventory, geographic])}
    return uriel_features


langs = ["bg", "cs", "da", "de", "el", "es", "et", "fi", "fr", "hu", 
         "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv"]
langs_3 = [iso639.languages.get(alpha2=l).part3 for l in langs]
lang2lang3 = {l: l3 for l, l3 in zip(langs, langs_3)}
xmi = pd.read_csv("../../results/test/xmi.mt.csv").set_index(["src", "tgt"])
pair2xmi = xmi.to_dict()['value']

uriel = uriel_distance_vec([iso639.languages.get(alpha2='en').part3]+[lang2lang3[s] for s in langs])

print('Into En')
print('Distance\t Pearson\t\t Spearman')
for k, v in uriel.items():
    losses = []
    distances = []
    for ix, l in enumerate(langs):
        losses.append(pair2xmi[(l, 'en')])
        distances.append(v[0,ix+1])
    pearsonr, pearsonp = stats.pearsonr(losses, distances)
    spearmanr, spearmanp = stats.spearmanr(losses, distances)
    print(k, '\t', '%.4f' % pearsonr, '(%.4f)'% pearsonp, '\t', '%.4f' % spearmanr, '(%.4f)' % spearmanp)

print('From En')
print('Distance\t Pearson\t\t Spearman')
for k, v in uriel.items():
    losses = []
    distances = []
    for ix, l in enumerate(langs):
        losses.append(pair2xmi[('en', l)])
        distances.append(v[0,ix+1])
    pearsonr, pearsonp = stats.pearsonr(losses, distances)
    spearmanr, spearmanp = stats.spearmanr(losses, distances)
    print(k, '\t', '%.4f' % pearsonr, '(%.4f)'% pearsonp, '\t', '%.4f' % spearmanr, '(%.4f)' % spearmanp)

print('Both')
print('Distance\t Pearson\t\t Spearman')
for k, v in uriel.items():
    losses = []
    distances = []
    for ix, l in enumerate(langs):
        losses.append(pair2xmi[('en', l)])
        distances.append(v[0,ix+1])
        losses.append(pair2xmi[(l, 'en')])
        distances.append(v[0,ix+1])
    pearsonr, pearsonp = stats.pearsonr(losses, distances)
    spearmanr, spearmanp = stats.spearmanr(losses, distances)
    print(k, '\t', '%.4f' % pearsonr, '(%.4f)'% pearsonp, '\t', '%.4f' % spearmanr, '(%.4f)' % spearmanp)


# Saving features
for k, v in uriel.items():
    with open('../../results/features/%s.wrt_en.csv' % k, 'w') as f:
        f.write('lang,value\n')
        for ix, l in enumerate(langs):
            f.write(l + ',%f\n' % v[0,ix+1])

