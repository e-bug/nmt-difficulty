#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preview'] = True
plt.rc('font', family='serif', serif=['Times'])

# missing en:
LANGS = list("bg cs da de el es et fi fr hu it lt lv nl pl pt ro sk sl sv".split())

xent_lm = pd.read_csv("../../results/test/xent.lm.csv").rename(columns={"lang": "tgt"}).set_index("tgt")
xent_mt = pd.read_csv("../../results/test/xent.mt.csv").set_index(["src", "tgt"])
xmi = pd.read_csv("../../results/test/xmi.mt.csv").set_index(["src", "tgt"])
assert all((xmi - (xent_lm - xent_mt)).abs() < 0.000001)


fig, ax = plt.subplots(figsize=(11, 3))
langscore = lambda l: float(xent_lm.loc[l])
langs_indices = np.argsort(np.array([langscore(l) for l in LANGS]))
width = 0.4
tab1 = (0.12, 0.46, 0.70)
tab2 = (1.0, 0.5, 0.05)
circle = "\\circ"
for i, (slicer, S, T) in enumerate([
        (pd.IndexSlice[:, "en"], circle, "\\texttt{en}"),
        (pd.IndexSlice["en", :], "\\texttt{en}", circle),
    ]):
    lower = xmi.loc[slicer, :]
    upper = xent_mt.loc[slicer, :]
    t1 = tuple((v*(1-.3*i) for v in tab1))
    t2 = tuple((v*(1-.3*i) for v in tab2))
    ax.bar([x + width*i for x in range(len(LANGS))], lower.values[langs_indices, 0], width=width, label=f"$\\mathrm{{XMI}}({S} \\to {T})$", color=t1)
    ax.bar([x + width*i for x in range(len(LANGS))], upper.values[langs_indices, 0], width=width, label=f"$\\mathrm{{H}}_{{q_{{\\mathrm{{MT}}}}}}({T} \mid {S})$", color=t2, bottom=lower.values[langs_indices, 0])
    for x, (lo, hi) in enumerate(zip(lower.values[langs_indices, 0], upper.values[langs_indices, 0])):
        ax.text(x + .03 + width*i, lo      - 5, f"\\bf {lo:.1f}", ha="center", va="top", color="white", rotation=90)
        ax.text(x + .03 + width*i, lo + hi - 5, f"\\bf {hi:.1f}", ha="center", va="top", color="white", rotation=90)
        if T == circle:
            ax.text(x + width*i, lo + hi + 5, f"{lo+hi:.0f}", ha="center", color="black")

threshold = int(xent_lm.loc["en"])
plt.axhline(y=threshold, linewidth=1, color='gray', linestyle='-.', zorder=-1, label="$\\mathrm{H}_{q_{\\mathrm{LM}}}(\\texttt{en})$")
ax.text(-1, threshold+5, "%d" % threshold, color="gray")

ax.set_ylabel("$\\mathrm{H}_{q_{\\mathrm{LM}}}(T)$")
ax.legend(loc="lower center", ncol=5)
ax.set_ylim(0, 185)
ax.set_xticks([x + width/2 for x in range(len(LANGS))])
ax.set_xticklabels([LANGS[i] for i in langs_indices])
ax.set_xlim(- .5, len(LANGS) - .1)

fig.tight_layout()
plt.savefig("results_stack.pdf")
