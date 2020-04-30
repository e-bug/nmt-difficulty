#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

langs = ['bg', 'cs', 'da', 'de', 'el', 'es', 'et', 'fi', 'fr', 'hu', 
         'it', 'lt', 'lv', 'nl', 'pl', 'pt', 'ro', 'sk', 'sl', 'sv']
exp_dir = '../../experiments/'

for split in ['valid', 'test']:
    pair2nll = {}
    pair2ppl = {}
    pair2xent = {}
    pair2xmi = {}
    pair2bleu = {}
    for lang in langs:
        score_fn = os.path.join(exp_dir, '%s2en/loss/loss.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        pair2nll[lang+',en'] = score
        score_fn = os.path.join(exp_dir, 'en2%s/loss/loss.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        pair2nll['en,'+lang] = score

        score_fn = os.path.join(exp_dir, '%s2en/ppl/ppl.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        pair2ppl[lang+',en'] = score
        score_fn = os.path.join(exp_dir, 'en2%s/ppl/ppl.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        pair2ppl['en,'+lang] = score

        score_fn = os.path.join(exp_dir, '%s2en/xent/xent.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        pair2xent[lang+',en'] = score
        score_fn = os.path.join(exp_dir, 'en2%s/xent/xent.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        pair2xent['en,'+lang] = score

        score_fn = os.path.join(exp_dir, '%s2en/xmi/xmi.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        pair2xmi[lang+',en'] = score
        score_fn = os.path.join(exp_dir, 'en2%s/xmi/xmi.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0])
        pair2xmi['en,'+lang] = score

        score_fn = os.path.join(exp_dir, '%s2en/bleu/bleu.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0].split(' = ')[1].split()[0])
        pair2bleu[lang+',en'] = score
        score_fn = os.path.join(exp_dir, 'en2%s/bleu/bleu.%s' % (lang, split))
        score = float(open(score_fn).readlines()[0].split(' = ')[1].split()[0])
        pair2bleu['en,'+lang] = score

    with open('../../results/%s/nll.mt.csv' % split, 'w') as f:
        f.write('src,tgt,value\n')
        for pair in sorted(pair2nll.keys()):
            f.write(pair + ',' + str(pair2nll[pair]) + '\n')

    with open('../../results/%s/ppl.mt.csv' % split, 'w') as f:
        f.write('src,tgt,value\n')
        for pair in sorted(pair2ppl.keys()):
            f.write(pair + ',' + str(pair2ppl[pair]) + '\n')

    with open('../../results/%s/xent.mt.csv' % split, 'w') as f:
        f.write('src,tgt,value\n')
        for pair in sorted(pair2xent.keys()):
            f.write(pair + ',' + str(pair2xent[pair]) + '\n')

    with open('../../results/%s/xmi.mt.csv' % split, 'w') as f:
        f.write('src,tgt,value\n')
        for pair in sorted(pair2xmi.keys()):
            f.write(pair + ',' + str(pair2xmi[pair]) + '\n')

    with open('../../results/%s/bleu.mt.csv' % split, 'w') as f:
        f.write('src,tgt,value\n')
        for pair in sorted(pair2bleu.keys()):
            f.write(pair + ',' + str(pair2bleu[pair]) + '\n')

