#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Evguenia Kopylova.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import sys
import os
from subprocess import Popen, PIPE

from numpy import array, mean, zeros
import matplotlib as mpl

mpl.use('agg')

import matplotlib.pyplot as plt
import brewer2mpl


def color_bp(bp, color):
    c = array(color) * 0.5
    c = tuple(c)

    for x in bp['boxes']:
        plt.setp(x, color=c)
        x.set_facecolor(color)
    for x in bp['medians']:
        plt.setp(x, color=c)
    for x in bp['whiskers']:
        plt.setp(x, color=c)
    for x in bp['fliers']: 
        plt.setp(x, color=c)
    for x in bp['caps']:
        plt.setp(x, color=c)


# code (modified) from https://github.com/samfway/biotm/blob/master/plotting/grouped_box.py
def make_separated_box(ax, data, labels=None, colors=None,
                       xticklabels=[], width=0.8, legend_pos=0,
                       dot_mean=False, mean_color='w'):
    if labels and len(data) != len(labels):
        raise ValueError('Number of labels must match ',
                         'size of data matrix.')

    if colors and len(colors) != len(labels):
        raise ValueError('Number of colors must match ',
                         'size of data matrix.')

    num_groups = len(labels)
    num_points = data.shape[1]

    if not colors:
        num_colors = max(3, num_groups)
        colors = brewer2mpl.get_map('Set2',
                                    'qualitative',
                                    num_colors).mpl_colors
    current_pos = 0
    xticks = []
    xlabels = []

    for i in xrange(num_groups):
        color = colors[i]
        for j in xrange(num_points):
            bp = ax.boxplot(data[i][j], positions=[current_pos],
                            widths=[width], patch_artist=True)
            xticks.append(current_pos)
            xlabels.append(xticklabels[j] + " (%s)" % len(data[i][j]))
            color_bp(bp, color)
            if dot_mean:
                means = [mean(data[i][j])]
                ax.plot([current_pos], means, linestyle='None', 
                    marker='o', markerfacecolor=mean_color,
                    markeredgecolor='k')
            current_pos += 1.6
        current_pos += 2

    if labels:
        lgd = legend_hack(ax, labels, colors, legend_pos)
    else:
        lgd = None

    ax.set_xlim(-1, current_pos-2)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)

    return lgd


def legend_hack(ax, labels, colors, legend_pos):
    """ Hack a legend onto a plot. 
    """ 
    handles = []
    for i, l in enumerate(labels):
        temp = plt.Line2D(range(1), range(1), 
                          linewidth=2,
                          color=colors[i])
        handles.append(temp)
    #plt.legend(handles, labels, numpoints=1, loc=legend_pos)
    lgd = plt.legend(handles, labels, numpoints=1, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #lgd = plt.legend(handles, labels, numpoints=1, bbox_to_anchor=(0, -0.7), loc='lower left', borderaxespad=0.)
    for handle in handles:
        handle.set_visible(False)

    return lgd 

def main():
    """Run single rarefaction on EMP tables & plot
    """
    gg_biom_fp = sys.argv[1]
    gg_tree_fp = sys.argv[2]
    si_biom_fp = sys.argv[3]
    si_tree_fp = sys.argv[4]
    outdir_dp = sys.argv[5]
    # e.g., "PD_whole_tree,chao1,observed_otus,shannon"
    alpha_metrics = sys.argv[6]
    data = {}
    data[gg_biom_fp] = gg_tree_fp
    data[si_biom_fp] = si_tree_fp
    sample_depths = ['1000', '10000', '30000', '100000', '1000000', '2000000']
    for key, value in data.iteritems():
        biom_fp = key
        tree_fp = value
        if not os.path.isfile(biom_fp):
            raise ValueError("%s doesn't exist" % biom_fp)
        if not os.path.isfile(tree_fp):
            raise ValueError("%s doesn't exist" % tree_fp)
        name = os.path.dirname(biom_fp).split('/')[-1]
        outdir = os.path.join(outdir_dp, name)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        for depth in sample_depths:
            if not os.path.isfile(os.path.join(outdir, "otu_table_even%s.biom" % depth)):
                single_rare_command = ["single_rarefaction.py",
                                       "-i",
                                       biom_fp,
                                       "-o",
                                       os.path.join(outdir, "otu_table_even%s.biom" % depth),
                                       "-d",
                                       depth]
                print "[command] = %s" % single_rare_command
                proc = Popen(single_rare_command,
                             stdout=PIPE,
                             stderr=PIPE,
                             close_fds=True)
                proc.wait()
                stdout, stderr = proc.communicate()
                if stderr:
                    print stderr
            else:
                print "Skipping %s, already exists" % os.path.join(outdir, "otu_table_even%s.biom" % depth)

    labels = []
    for key, value in data.iteritems():
        biom_fp = key
        tree_fp = value
        name = os.path.dirname(biom_fp).split('/')[-1]
        labels.append(name)
        outdir = os.path.join(outdir_dp, name)
        for depth in sample_depths:
            if not os.path.isfile(os.path.join(outdir, "alpha_div_even%s.txt" % depth)):
                alpha_div_command = ["alpha_diversity.py",
                                     "-i",
                                     os.path.join(outdir, "otu_table_even%s.biom" % depth),
                                     "-o",
                                     os.path.join(outdir, "alpha_div_even%s.txt" % depth),
                                     "-t",
                                     tree_fp,
                                     "-m",
                                     alpha_metrics]
                print "[command] = %s" % alpha_div_command
                proc = Popen(alpha_div_command,
                             stdout=PIPE,
                             stderr=PIPE,
                             close_fds=True)
                proc.wait()
                stdout, stderr = proc.communicate()
                if stderr:
                    print stderr
            else:
                print "Skipping %s, already exists" % os.path.join(outdir, "alpha_div_even%s.txt" % depth)

    num_groups = len(data)
    num_time_points = len(sample_depths)
    xticklabels = sample_depths
    data_oo = zeros((num_groups, num_time_points), dtype=list)
    data_pd = zeros((num_groups, num_time_points), dtype=list)
    data_ch = zeros((num_groups, num_time_points), dtype=list)
    data_sh = zeros((num_groups, num_time_points), dtype=list)

    print "Computing graphs ..."
    for i, (key, value) in enumerate(data.items()):
        for j, depth in enumerate(sample_depths):
            biom_fp = key
            name = os.path.dirname(biom_fp).split('/')[-1]
            outdir = os.path.join(outdir_dp, name)
            file_s = os.path.join(outdir, "alpha_div_even%s.txt" % depth)
            pd_list = []
            oo_list = []
            ch_list = []
            sh_list = []
            with open(file_s, 'U') as collection:
                next(collection)
                for line in collection:
                    line = line.strip().split()
                    pd_whole_tree = float(line[1])
                    chao1 = float(line[2])
                    observed_otus = float(line[3])
                    shannon = float(line[4])
                    pd_list.append(pd_whole_tree)
                    oo_list.append(observed_otus)
                    ch_list.append(chao1)
                    sh_list.append(shannon)
                data_oo[i][j] = oo_list
                data_pd[i][j] = pd_list
                data_ch[i][j] = ch_list
                data_sh[i][j] = sh_list                  

    # observed OTUs
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.set_title('Study %s: Alpha rarefaction at various depths (sequences/sample)' % study)
    ax.set_xticklabels(xticklabels, rotation=40, ha='center')
    ax.set_ylabel('observed_otus')
    ax.set_xlabel('sampling depths (# of samples)')
    lgd = make_separated_box(ax, data_oo, labels, xticklabels=xticklabels, legend_pos='lower right')
    lgd = None

    plots_dir = os.path.join(outdir_dp, name, "plots")
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    fig.savefig(os.path.join(plots_dir, 'observed_otus.png'), bbox_inches='tight')

    # PD_whole_tree
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticklabels(labels, rotation=40, ha='center')
    ax.set_ylabel("Faith's phylogenetic diversity (PD_whole_tree)")
    ax.set_xlabel('sampling depth (# of samples)')
    lgd = make_separated_box(ax, data_pd, labels, xticklabels=xticklabels, legend_pos='lower right')
    
    fig.savefig(os.path.join(plots_dir, 'pd_whole_tree.png'), bbox_extra_artists=(lgd,), bbox_inches='tight')

    # Shannon
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticklabels(labels, rotation=40, ha='center')
    ax.set_ylabel("Shannon index")
    ax.set_xlabel('sampling depth (# of samples)')
    lgd = make_separated_box(ax, data_sh, labels, xticklabels=xticklabels, legend_pos='lower right')
    
    fig.savefig(os.path.join(plots_dir, 'shannon.png'), bbox_extra_artists=(lgd,), bbox_inches='tight')

    # chao1
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticklabels(labels, rotation=40, ha='center')
    ax.set_ylabel("Chao1 index")
    ax.set_xlabel('sampling depth (# of samples)')
    lgd = make_separated_box(ax, data_ch, labels, xticklabels=xticklabels, legend_pos='lower right')
    
    fig.savefig(os.path.join(plots_dir, 'chao1.png'), bbox_extra_artists=(lgd,), bbox_inches='tight')

if __name__ == '__main__':
    main()

