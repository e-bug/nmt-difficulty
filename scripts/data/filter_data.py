import glob
import os.path
import argparse
import numpy as np
from collections import defaultdict, Counter


# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--data-dir', required=True)
args = parser.parse_args()

# Files
en_fns = glob.glob(os.path.join(args.data_dir, 'train.*-en.tok.clean.en'))

# Get clean data
src2sentcount = dict()
src2clean = dict()
langs = []
for fn in en_fns:
    with open(fn, 'r', encoding='utf-8') as f:
        clean_lines = f.readlines()
    lang = fn.split('/')[-1].split('.')[1].split('-')[0]
    src2sentcount[lang] = Counter(clean_lines)
    src2clean[lang] = np.array(clean_lines)
    langs.append(lang)

# Find new overlapping sentences
lowest_lang = list(src2clean.keys())[np.argmin([len(ll) for ll in src2clean.values()])]
line2noverlapping = dict()
for l, c in src2sentcount[lowest_lang].items():
    list_ = []
    for k in langs:
        c = src2sentcount[k].get(l, None)
        list_.append(c)
    if list_.count(None) == 0:
        line2noverlapping[l] = min(list_)
        
src2overlapixs = defaultdict(list)
src2line2ixs = defaultdict(dict)
for k, v in src2clean.items():
    k_line2ixs = defaultdict(list)
    for ix,line in enumerate(v):
        if line in line2noverlapping.keys() and len(k_line2ixs[line]) < line2noverlapping[line]:
            k_line2ixs[line].append(ix)
            src2overlapixs[k].append(ix)
    src2line2ixs[k] = k_line2ixs

# Save filtered data
for k, l2ixs in src2line2ixs.items():
    with open(os.path.join(args.data_dir, 'train.%s-en.tok.clean.%s' % (k, k)), 'r', encoding='utf-8') as f:
        k_lines = f.readlines()
    with open(os.path.join(args.data_dir, 'train.%s-en.tok.clean.filt.%s' % (k, k)), 'w', encoding='utf-8') as f:
        for ix in src2overlapixs[k]:
            f.write(k_lines[ix])
    with open(os.path.join(args.data_dir, 'train.%s-en.tok.clean.filt.en' % k), 'w', encoding='utf-8') as f:
        for ix in src2overlapixs[k]:
            f.write(src2clean[k][ix])

