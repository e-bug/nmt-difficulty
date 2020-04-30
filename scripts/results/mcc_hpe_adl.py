#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import pandas as pd

def get_correlations(lang2metric, pair2xmi, where='src', name=None):
    xs = []
    ys = []
    for l, val in lang2metric.items():
        if l == 'en':
            continue
        if where == 'src':
            xmi = pair2xmi[(l, 'en')]
            xs.append(val)
            ys.append(xmi)
        elif where == 'tgt':
            xmi = pair2xmi[('en', l)]
            xs.append(val)
            ys.append(xmi)
        else:
            xmi = pair2xmi[(l, 'en')]
            xs.append(val)
            ys.append(xmi)
            xmi = pair2xmi[('en', l)]
            xs.append(val)
            ys.append(xmi)
    if not name:
        name = ''
    pearson_r, pearson_p = stats.pearsonr(xs, ys)
    spearman_rho, spearman_p = stats.spearmanr(xs, ys)
    print(name, '\t', '%.4f' % pearson_r, '(%.4f)'% pearson_p, '\t', '%.4f' % spearman_rho, '(%.4f)' % spearman_p)


mcc = pd.read_csv("../../results/features/mcc.csv").set_index("lang")
lang2mcc = mcc.to_dict()['value']
adl = pd.read_csv("../../results/features/adl.csv").set_index("lang")
lang2adl = adl.to_dict()['value']
hpe = pd.read_csv("../../results/features/hpe.csv").set_index("lang")
lang2hpe = hpe.to_dict()['value']
xmi = pd.read_csv("../../results/test/xmi.mt.csv").set_index(["src", "tgt"])
pair2xmi = xmi.to_dict()['value']


print('Into En')
print('Distance\t Pearson\t\t Spearman')
get_correlations(lang2mcc, pair2xmi, where='src', name='MCC')
get_correlations(lang2adl, pair2xmi, where='src', name='ADL')
get_correlations(lang2hpe, pair2xmi, where='src', name='HPE-mean')

print('From En')
print('Distance\t Pearson\t\t Spearman')
get_correlations(lang2mcc, pair2xmi, where='tgt', name='MCC')
get_correlations(lang2adl, pair2xmi, where='tgt', name='ADL')
get_correlations(lang2hpe, pair2xmi, where='tgt', name='HPE-mean')

print('Both')
print('Distance\t Pearson\t\t Spearman')
get_correlations(lang2mcc, pair2xmi, where='both', name='MCC')
get_correlations(lang2adl, pair2xmi, where='both', name='ADL')
get_correlations(lang2hpe, pair2xmi, where='both', name='HPE-mean')
