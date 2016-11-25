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
import glob

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


def make_separated_box(ax, data, labels=None, colors=None,
                       xticklabels=[], width=0.8, legend_pos=0,
                       dot_mean=False, mean_color='w'):
    """Make separated box plot.

    Notes
    -----
    code (modified) from
    https://github.com/samfway/biotm/blob/master/plotting/grouped_box.py
    """
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
            if not data[i][j]:
                current_pos += 1.6
                continue
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

    Notes
    -----
    code (modified) from
    https://github.com/samfway/biotm/blob/master/plotting/grouped_box.py
    """
    handles = []
    for i, l in enumerate(labels):
        temp = plt.Line2D(range(1), range(1),
                          linewidth=2,
                          color=colors[i])
        handles.append(temp)
    lgd = plt.legend(handles, labels, numpoints=1,
                     bbox_to_anchor=(0., 1.02, 1., .102), ncol=2,
                     mode="expand", loc=3, borderaxespad=0.)
    for handle in handles:
        handle.set_visible(False)

    return lgd


def parse_mapping_file(mapping_file_fp, mapping_column):
    """Parse the mapping file into a dict.

    Parameters
    ----------
    mapping_file: string
        path to mapping file
    mapping_column: string
        column ID in mapping file

    Returns
    -------
    mapping_dict: dictionary
        Dictionary with sample IDs as keys and mapping data as list in value
    mapping_column:
        Column in mapping file for which to use samples (e.g., EMPO_2)
    """
    mapping_dict = {}
    field_idx = None
    options = set()
    with open(mapping_file_fp) as f:
        for line in f:
            line = line.strip().split('\t')
            if line[0] == "#SampleID":
                if mapping_column in line:
                    field_idx = line.index(mapping_column)-1
                else:
                    raise ValueError(
                        "Column %s not in %s" % (
                            mapping_column, mapping_file_fp))
                continue
            if line[0].lower() not in mapping_dict:
                mapping_dict[line[0].lower()] = line[1:]
                options.add(line[field_idx+1])
            else:
                raise ValueError("Duplicate sample IDs %s" % line[0].lower())
    return mapping_dict, options, field_idx


def generate_plots(sample_depths, labels, ylabel, data, output_dir,
                   field_value, lgd=True):
    """Plot box plots for alpha diversity at different rarefied depths.

    Parameters
    ----------
    sample_depths: list
        List of rarefaction depths used as xticklabels
    labels: list
        List of methods tested (e.g., Greengenes and Silva databases)
    ylabel: string
        Alpha diversity metric
    data: numpy.array
        Alpha diversity for a specified metric for all methods
    output_dir: string
        path to output directory
    field_value: string
        Field value for which samples were chosen
    lgd: boolean
        If True, plot legend otherwise don't
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticklabels(sample_depths, rotation=40, ha='center')
    ax.set_ylabel(ylabel)
    ax.set_xlabel('sampling depth (# of samples)')
    if lgd:
        make_separated_box(ax, data, labels, xticklabels=sample_depths,
                           legend_pos='lower right')
    else:
        lgd = None
    plots_dir = os.path.join(output_dir, "plots")
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    if field_value != 'None':
        fig.savefig(os.path.join(
            plots_dir, '%s_%s.png' % (field_value, ylabel)),
            bbox_inches='tight')
    else:
        fig.savefig(os.path.join(plots_dir, '%s.png' % ylabel),
                    bbox_inches='tight')


def compute_data(metric, num_groups, num_time_points, groups, sample_depths,
                 labels, mapping_column, field_value, mapping_dict, field_idx):
    """Parse alpha diversity files for certain metric.

    Parameters
    ----------
    metric: string
        Alpha diversity metric (e.g., PD_whole_tree)
    num_groups: integer
        Number of methods (e.g., Greengenes and Silva = 2)
    num_time_points: integer
        Number of rarefaction depths
    groups: list
        List of directory paths to alpha diversity results for all methods
    sample_depths: list
        List of rarefaction depths
    labels: list
        Labels for all groups
    mapping_column: string
        Column in mapping file for which to use samples (e.g., EMPO_2)
    field_value: string
        One option from mapping_column column (e.g., Non-Saline)
    mapping_dict: dictionary
        Dictionary with sample IDs as keys and mapping data as list in value
    field_idx: integer
        Index in mapping file for mapping_column

    Returns
    -------
    data: numpy.array
        Alpha diversity for a specified metric for all methods
    """
    data = zeros((num_groups, num_time_points), dtype=list)
    for i, group_dp in enumerate(groups):
        for j, depth in enumerate(sample_depths):
            labels.add(group_dp.split('/')[-1])
            file_s = glob.glob("%s/*_%s.txt" % (group_dp, depth))[0]
            values = []
            alpha_metrics_idx = {}
            with open(file_s, 'U') as collection:
                line = collection.readline().strip().split('\t')
                for local_metric in line:
                    alpha_metrics_idx[local_metric] =\
                        line.index(local_metric)+1
                if metric not in alpha_metrics_idx:
                    raise ValueError(
                        "%s is not in the file %s" % (metric, file_s))
                for line in collection:
                    line = line.strip().split()
                    sample_id = line[0].lower()
                    # Don't put sample in graph if not correct field value
                    if mapping_column != 'None':
                        if mapping_dict[sample_id][field_idx] != field_value:
                            continue
                    idx = alpha_metrics_idx[metric]
                    value = float(line[idx])
                    values.append(value)
                data[i][j] = values
    return data


def main():
    """Plot alpha diversity using set of rarefied BIOM tables
    """
    alpha_dp = sys.argv[1]
    mapping_file = sys.argv[2]
    # e.g., EMPO_1
    mapping_column = sys.argv[3]
    # e.g., Host-associated
    field_value = sys.argv[4]
    # output directory
    output_dp = sys.argv[5]
    # alpha metrics to graph
    alpha_metrics = sys.argv[6].split(',')
    # number of groups
    groups = sorted(glob.glob("%s/*" % alpha_dp))
    num_groups = len(groups)
    # rarefied sample depths
    sample_depths = ['1000', '10000', '30000', '100000', '1000000', '2000000']
    mapping_dict = {}
    field_idx = None
    if mapping_column != 'None':
        mapping_dict, options, field_idx = parse_mapping_file(
            mapping_file, mapping_column)
    labels = set()
    num_time_points = len(sample_depths)
    print("Computing graphs ...")
    for metric in alpha_metrics:
        data = compute_data(
            metric, num_groups, num_time_points, groups, sample_depths,
            labels, mapping_column, field_value, mapping_dict, field_idx)
        generate_plots(
            sample_depths, sorted(list(labels)), metric, data, output_dp,
            field_value, lgd=True)


if __name__ == '__main__':
    main()
