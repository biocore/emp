#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Evguenia Kopylova.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import sys
import numpy as np


def union(a, b):
    """Return the union of two lists.
    """
    return list(set(a) | set(b))


def intersect(a, b):
    """Return the intersection of two lists.
    """
    return list(set(a) & set(b))


def sample_ids(file_fp):
    """Return list of sample IDs parsed from alpha diversity file.

    Parameters
    ----------
    file_fp: string
        filepath to alpha diversity file (output of alpha_diversity.py)

    Returns
    -------
    sample_ids: list
        list of sample IDs
    """
    sample_ids = []
    # read alpha div file
    with open(file_fp) as file_f:
        next(file_f)
        for line in file_f:
            line = line.strip().split('\t')
            sample_id = line[0].lower()
            if sample_id not in sample_ids:
                sample_ids.append(sample_id)
            else:
                raise ValueError(
                    "Duplicate sample ID %s in %s" % (sample_id, file_fp))
    return sample_ids


def get_metrics(file_fp, all_sample_ids, metric):
    """Return ordered list with alpha div metrics for all samples.

    Parameters
    ----------
    file_fp: string
        filepath to alpha diversity file (output of alpha_diversity.py)
    all_sample_ids: list
        list of sample IDs to observe (e.g., union or intersection between
        samples IDs in two alpha diversity files rarefied to same depth)
    metric: string
        alpha diversity metric (e.g., PD_whole_tree, observed_otus, etc.)

    Returns
    -------
    list: list
        ordered list with alpha diversity values for all samples
    """
    sample_ids = {id_: 0.0 for id_ in all_sample_ids}
    # read alpha div file
    with open(file_fp) as file_f:
        # list of metrics
        header = file_f.readline().strip().split('\t')
        if metric not in header:
            raise ValueError("%s not in %s" % (metric, file_fp))
        metric_idx = header.index(metric)
        for line in file_f:
            line = line.strip().split('\t')
            if line[0] in sample_ids:
                sample_ids[line[0]] = line[metric_idx+1]
    return sorted(sample_ids.items())


def compute_outliers(metric_a, metric_b, offset):
    """Return samples whose metric difference is an outlier.

    Parameters
    ----------
    metric_a: list
        list of sample IDs and associated metric values for database 1
    metric_b: list
        list of sample IDs and associated metric values for database 2
    offset: float
        IQR offset for computing outliers

    Returns
    -------
    outliers: list
        list of sample IDs

    Notes
    -----
    Outliers are computed by taking the difference between a metric value
    for two identical samples in both databases and using the list of
    differences to compute the interquartile range (IQR). The first and
    third quartiles of the IQR are multipled by the first to give the upper
    and lower bounds of outliers. Samples with differences outside the bounds
    are returned as outliers.
    """
    metric_a_array = np.array([b for a, b in metric_a], dtype=float)
    metric_b_array = np.array([b for a, b in metric_b], dtype=float)
    outliers = []
    differences = np.absolute(metric_a_array - metric_b_array)
    q75, q25 = np.percentile(differences, [75, 25])
    iqr = q75 - q25
    upper_bound = q75 + iqr*float(offset)
    lower_bound = q25 - iqr*float(offset)
    for i, diff in enumerate(differences):
        if (diff > upper_bound) or (diff < lower_bound):
            outliers.append(metric_a[i][0])
    return outliers


def main():
    """Compute the mean & standard deviation for the set of differences
       in an alpha diversity metric for two datasets (rarefied at the same
       depth) and report samples whose differences are 2*std_dev away from
       the mean
    """
    gg_alpha_fp = sys.argv[1]
    si_alpha_fp = sys.argv[2]
    metric = sys.argv[3]
    # IQR offset for outliers
    offset = float(sys.argv[4])
    # Keep samples which occur only in one dataset
    keep_unique_samples = sys.argv[5]
    # list of sample IDs, verify they are unique in file
    sample_ids_gg = sample_ids(gg_alpha_fp)
    sample_ids_si = sample_ids(si_alpha_fp)
    # union of sample IDs between two files (if we want to include all
    # samples between both files)
    if keep_unique_samples == "True":
        sample_ids_filter = union(sample_ids_gg, sample_ids_si)
    # intersection of sample IDs between two files (if we want to include
    # only samples found in both files)
    else:
        sample_ids_filter = intersect(sample_ids_gg, sample_ids_si)
    samples_in_gg_not_silva = list(set(sample_ids_gg) - set(sample_ids_si))
    samples_in_silva_not_gg = list(set(sample_ids_si) - set(sample_ids_gg))
    print "samples_in_gg_not_silva = ", samples_in_gg_not_silva
    print "samples_in_silva_not_gg = ", samples_in_silva_not_gg
    # associate metric values with sample IDs
    metric_gg = get_metrics(gg_alpha_fp, sample_ids_filter, metric)
    metric_si = get_metrics(si_alpha_fp, sample_ids_filter, metric)
    # output outlier samples
    outliers = compute_outliers(metric_gg, metric_si, offset)
    ratio_outliers = float(len(outliers))/float(len(sample_ids_filter))*100.0
    sys.stdout.write("{0:.2f}".format(ratio_outliers))

    print "outliers = ", outliers
    print ""


if __name__ == '__main__':
    main()
