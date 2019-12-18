"""
We will make two plots:
    - Windowed nucleotide diversity
    - Site frequency spectrum
"""
import os
import sys
import numpy as np
import allel

import matplotlib.pyplot as plt
import seaborn as sns


def usage():
    print(f"usage: {sys.argv[0]} path_to_vcf path_to_plot_dir")
    exit(1)


try:
    vcf_fname = sys.argv[1]
    plot_dir = sys.argv[2]
except IndexError:
    usage()

for path in [vcf_fname, plot_dir]:
    if not os.path.exists(path):
        print(f"Cannot find {path}")
        usage()


def plot_windowed_pi(
    pi, bins, title=None, dest=os.path.join(plot_dir, "nuc_diversity.pdf")
):
    """
    Credit: http://alimanfoo.github.io/2016/06/10/scikit-allel-tour.html
    """

    # use window midpoints as x coordinate
    x = (bins[:, 0] + bins[:, 1]) / 2

    # plot
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.despine(ax=ax, offset=9)
    ax.plot(x, pi)
    ax.set_xlabel("Genome position (bp)")
    ax.set_ylabel("$pi$")
    if title:
        ax.set_title(title)

    fig.savefig(dest)


def plot_sfs(allele_counts, dest=os.path.join(plot_dir, "site_freq_spectrum.pdf")):
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.despine(ax=ax, offset=10)
    sfs = allel.sfs_folded(allele_counts)
    # sfs = sfs[1:-1]
    x = np.arange(0, sfs.shape[0])
    n = allele_counts.sum(axis=1).max()
    x = x / n  ## To frequencies
    # sns.barplot(x, sfs, ax=ax, color=sns.color_palette("Blues")[3])
    ax.plot(x, sfs)

    ##allel.plot_sfs_folded(sfs, ax=ax, label='TB', n=allele_counts.sum(axis=1).max())
    ##ax.legend()
    ax.set_title("Folded site frequency spectrum")
    # workaround bug in scikit-allel re axis naming
    ax.set_xlabel("minor allele frequency")
    ax.set_ylabel("num sites")

    fig.savefig(dest)


####Load genotype calls#####
callset = allel.read_vcf(vcf_fname, fields=["variants/POS", "calldata/GT"])
gt = allel.GenotypeArray(callset["calldata/GT"])


## Data preprocessing ##
non_het_variants = gt.count_het(axis=1) == 0
gt_clean = gt[
    non_het_variants
]  ## filter out sites with heterozygous calls, because TB is haploid
gt_clean = gt_clean.haploidify_samples()  ## Convert to haploid calls

pos = callset["variants/POS"][non_het_variants]  ## The retained variant positions

#######Plot 1: nucleotide diversity#########
allele_counts = gt_clean.count_alleles()

window_size = int((pos[-1] - pos[0]) / 100)  # We want about 100 windows
pi, windows, n_bases, n_counts = allel.windowed_diversity(
    pos, allele_counts, size=window_size, start=pos[0], stop=pos[-1]
)

plot_windowed_pi(pi, windows)

######Plot 2: site frequency spectrum########
## Filtering : only keep biallelic variants (at most two alleles segregate in the set of samples)
max_2_alleles = [sum(row != 0) <= 2 for row in allele_counts]
filtered_ac = allele_counts[max_2_alleles]
bi_counts = allel.AlleleCountsArray(np.ndarray((filtered_ac.shape[0], 2), dtype=int))
index = 0
for row in filtered_ac:
    picked = [i for i in row if i != 0]
    assert len(picked) <= 2
    if len(picked) == 1:
        picked = picked + [0]
    elif len(picked) == 0:
        picked = [0, 0]
    bi_counts[index] = picked
    index += 1

plot_sfs(bi_counts)
