import glob
import os.path
import argparse
import numpy as np
from collections import defaultdict, Counter

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', required=True)
parser.add_argument('--output-dir', required=True)
args = parser.parse_args()

# Files
files = glob.glob(os.path.join(args.input_dir, '*'))
en_files = glob.glob(os.path.join(args.input_dir, '*.en'))
src_files = list(set(files).difference(en_files))
src2fn = {fn.split('-')[-2][3:]: fn[:-2] for fn in en_files}

# Get indices of empty lines in non-English files
src2empty_ixs = dict()
for k, v in src2fn.items():
    with open(v + k, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    src2empty_ixs[k] = set([ix for ix,l in enumerate(lines) if l == '\n'])

# Get En sentences
src2en_lines = dict()
for k, v in src2fn.items():
    with open(v + 'en') as f:
        src2en_lines[k] = f.readlines()
    
# Indices of empty En lines
src2en_empty_ixs = dict()
for k, v in src2en_lines.items():
    src2en_empty_ixs[k] = set([ix for ix,l in enumerate(v) if l == '\n'])
    
# Remove En lines that are empty at either src or tgt
src2nonempty_lines = dict()
for k, v in src2en_lines.items():
    src2nonempty_lines[k] = [l for ix,l in enumerate(v) 
                             if (ix not in src2empty_ixs[k] and ix not in src2en_empty_ixs[k])]

# Number of overlapping sentences
lowest_lang = list(src2nonempty_lines.keys())[np.argmin([len(l) for l in src2nonempty_lines.values()])]
min_lines = src2nonempty_lines[lowest_lang]
langs = src2nonempty_lines.keys()
nlangs = len(langs)
min_counter = Counter(min_lines)
src2counter = {k: Counter(v) for k, v in src2nonempty_lines.items()}
overlapping_lines = []
for l, c in min_counter.items():
    l_count = []
    for k in langs:
        l_count.append(src2counter[k][l])
    overlapping_lines.extend([l] * min(l_count))
        
# Shared sentences corpora
counter = Counter(overlapping_lines)
src2overlapping_ixs = defaultdict(list)
for k, v in src2en_lines.items():
    k_lines = defaultdict(int)
    for ix,line in enumerate(v):
        if line in counter.keys() and k_lines[line] < counter[line]:
            src2overlapping_ixs[k].append(ix)
            k_lines[line] += 1

# Align shared sentences across pairs
src2aligned_ixs = defaultdict(list)
for k, v in src2overlapping_ixs.items():
    line2ixs = defaultdict(list)
    for ix in v:
        line2ixs[src2en_lines[k][ix]].append(ix)
    for l, c in counter.items():
        src2aligned_ixs[k].extend(line2ixs[l])

# Split into train, valid and test ensuring no overlaps in test set
np.random.seed(1234)
rnd_ixs = np.random.choice(len(overlapping_lines), size=len(overlapping_lines), replace=False)
train_ixs, valid_ixs, test_ixs = [], [], []
valid_en, test_en = set(), set()
for ix in rnd_ixs:
    en = src2en_lines['pt'][src2aligned_ixs['pt'][ix]]
    if en not in test_en and len(test_en) < 2000:
        test_en.add(en)
        test_ixs.append(ix)
    elif en not in valid_en and len(valid_en) < 1000:
        valid_en.add(en)
        valid_ixs.append(ix)
already_set = set(valid_ixs).union(test_ixs)
train_ixs = [ix for ix in rnd_ixs if ix not in already_set]

# Save aligned data 
for k, ixs in src2aligned_ixs.items():
    with open(os.path.join(args.input_dir, 'europarl-v7.%s-en.%s' % (k, k)), 'r', encoding='utf-8') as f:
        k_lines = f.readlines()
    with open(os.path.join(args.output_dir, 'train.%s-en.%s' % (k, k)), 'w', encoding='utf-8') as f:
        for ix in train_ixs:
            f.write(k_lines[ixs[ix]])
    with open(os.path.join(args.output_dir, 'train.%s-en.en' % k), 'w', encoding='utf-8') as f:
        for ix in train_ixs:
            f.write(src2en_lines[k][ixs[ix]])
    with open(os.path.join(args.output_dir, 'valid.%s-en.%s' % (k, k)), 'w', encoding='utf-8') as f:
        for ix in valid_ixs:
            f.write(k_lines[ixs[ix]])
    with open(os.path.join(args.output_dir, 'valid.%s-en.en' % k), 'w', encoding='utf-8') as f:
        for ix in valid_ixs:
            f.write(src2en_lines[k][ixs[ix]])
    with open(os.path.join(args.output_dir, 'test.%s-en.%s' % (k, k)), 'w', encoding='utf-8') as f:
        for ix in test_ixs:
            f.write(k_lines[ixs[ix]])
    with open(os.path.join(args.output_dir, 'test.%s-en.en' % k), 'w', encoding='utf-8') as f:
        for ix in test_ixs:
            f.write(src2en_lines[k][ixs[ix]])

