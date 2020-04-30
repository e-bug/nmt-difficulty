#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

langs = ['bg', 'cs', 'da', 'de', 'el', 'es', 'et', 'fi', 'fr', 'hu', 
         'it', 'lt', 'lv', 'nl', 'pl', 'pt', 'ro', 'sk', 'sl', 'sv']
exp_dir = '../../experiments/'

for split in ['valid', 'test']:
    lang2nll = {}
    lang2ppl = {}
    lang2xent = {}
    for lang in langs + ['en']:
        score_fn = os.path.join(exp_dir, '%s/loss/loss.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        lang2nll[lang] = score

        score_fn = os.path.join(exp_dir, '%s/ppl/ppl.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        lang2ppl[lang] = score

        score_fn = os.path.join(exp_dir, '%s/xent/xent.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        lang2xent[lang] = score

    with open('../../results/%s/nll.lm.csv' % split, 'w') as f:
        f.write('lang,value\n')
        for lang in sorted(lang2nll.keys()):
            f.write(lang + ',' + str(lang2nll[lang]) + '\n')

    with open('../../results/%s/ppl.lm.csv' % split, 'w') as f:
        f.write('lang,value\n')
        for lang in sorted(lang2ppl.keys()):
            f.write(lang + ',' + str(lang2ppl[lang]) + '\n')

    with open('../../results/%s/xent.lm.csv' % split, 'w') as f:
        f.write('lang,value\n')
        for lang in sorted(lang2xent.keys()):
            f.write(lang + ',' + str(lang2xent[lang]) + '\n')

