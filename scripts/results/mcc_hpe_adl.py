#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import pandas as pd

def get_correlations(df, name=None):
    xs = df.values[:, 0]
    ys = df.values[:, 1]
    pearson_r, pearson_p = stats.pearsonr(xs, ys)
    spearman_rho, spearman_p = stats.spearmanr(xs, ys)
    if not name:
        name = ''
    print(name, '\t', '%.4f' % pearson_r, '(%.4f)'% pearson_p, '\t', '%.4f' % spearman_rho, '(%.4f)' % spearman_p)


xmi = pd.read_csv("../../results/test/xmi.mt.csv").set_index(["src", "tgt"]).rename(columns={"value":"xmi"})

mcc_tgt = pd.read_csv("../../results/features/mcc.csv").rename(columns={"lang": "tgt"}).set_index("tgt").rename(columns={"value":"metric_tgt"})
mcc_src = pd.read_csv("../../results/features/mcc.csv").rename(columns={"lang": "src"}).set_index("src").rename(columns={"value":"metric_src"})
xmi_mcc = xmi.merge(mcc_tgt, left_index=True, right_index=True).merge(mcc_src, left_index=True, right_index=True)

adl_tgt = pd.read_csv("../../results/features/adl.csv").rename(columns={"lang": "tgt"}).set_index("tgt").rename(columns={"value":"metric_tgt"})
adl_src = pd.read_csv("../../results/features/adl.csv").rename(columns={"lang": "src"}).set_index("src").rename(columns={"value":"metric_src"})
xmi_adl = xmi.merge(adl_tgt, left_index=True, right_index=True).merge(adl_src, left_index=True, right_index=True)

hpe_tgt = pd.read_csv("../../results/features/hpe.csv").rename(columns={"lang": "tgt"}).set_index("tgt").rename(columns={"value":"metric_tgt"})
hpe_src = pd.read_csv("../../results/features/hpe.csv").rename(columns={"lang": "src"}).set_index("src").rename(columns={"value":"metric_src"})
xmi_hpe = xmi.merge(hpe_tgt, left_index=True, right_index=True).merge(hpe_src, left_index=True, right_index=True)


print('Into En')
print('Distance\t Pearson\t\t Spearman')
get_correlations(xmi_mcc.loc[pd.IndexSlice[:, 'en'], ['xmi', 'metric_src']], name='MCC_src')
get_correlations(xmi_mcc.loc[pd.IndexSlice[:, 'en'], ['xmi', 'metric_tgt']], name='MCC_tgt')
get_correlations(xmi_adl.loc[pd.IndexSlice[:, 'en'], ['xmi', 'metric_src']], name='ADL_src')
get_correlations(xmi_adl.loc[pd.IndexSlice[:, 'en'], ['xmi', 'metric_tgt']], name='ADL_tgt')
get_correlations(xmi_hpe.loc[pd.IndexSlice[:, 'en'], ['xmi', 'metric_src']], name='HPE_src')
get_correlations(xmi_hpe.loc[pd.IndexSlice[:, 'en'], ['xmi', 'metric_tgt']], name='HPE_tgt')

print('From En')
print('Distance\t Pearson\t\t Spearman')
get_correlations(xmi_mcc.loc[pd.IndexSlice['en', :], ['xmi', 'metric_src']], name='MCC_src')
get_correlations(xmi_mcc.loc[pd.IndexSlice['en', :], ['xmi', 'metric_tgt']], name='MCC_tgt')
get_correlations(xmi_adl.loc[pd.IndexSlice['en', :], ['xmi', 'metric_src']], name='ADL_src')
get_correlations(xmi_adl.loc[pd.IndexSlice['en', :], ['xmi', 'metric_tgt']], name='ADL_tgt')
get_correlations(xmi_hpe.loc[pd.IndexSlice['en', :], ['xmi', 'metric_src']], name='HPE_src')
get_correlations(xmi_hpe.loc[pd.IndexSlice['en', :], ['xmi', 'metric_tgt']], name='HPE_tgt')

print('Both')
print('Distance\t Pearson\t\t Spearman')
get_correlations(xmi_mcc.loc[:, ['xmi', 'metric_src']], name='MCC_src')
get_correlations(xmi_mcc.loc[:, ['xmi', 'metric_tgt']], name='MCC_tgt')
get_correlations(xmi_adl.loc[:, ['xmi', 'metric_src']], name='ADL_src')
get_correlations(xmi_adl.loc[:, ['xmi', 'metric_tgt']], name='ADL_tgt')
get_correlations(xmi_hpe.loc[:, ['xmi', 'metric_src']], name='HPE_src')
get_correlations(xmi_hpe.loc[:, ['xmi', 'metric_tgt']], name='HPE_tgt')

