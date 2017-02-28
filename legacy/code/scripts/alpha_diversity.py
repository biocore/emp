#!/usr/bin/env python

#-----------------------------------------------------------------------------
# Copyright (c) 2016--, Evguenia Kopylova, Daniel McDonald
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

"""
Alpha diversity using skbio.
"""

import click
import skbio
import biom
import numpy as np
import pandas as pd
from skbio.diversity import alpha_diversity


def compute_alpha_diversity(table,
                            metric,
                            **kwargs):
    """Compute Faith's phylogenetic diversity.

    Parameters
    ----------
    table: biom.table.Table object
        BIOM table
    metric: str
        alpha diversity metric
    kwargs: dict, optional
        Metric-specific parameters

    Returns
    -------
    results: pd.Series
        alpha diversity per sample
    """
    sample_ids = table.ids(axis='sample')
    counts = table.matrix_data.astype(int).T.toarray()
    results = alpha_diversity(metric=metric,
                              counts=counts,
                              ids=sample_ids,
                              validate=False,
                              **kwargs)
    results.name = metric
    return results


@click.command()
@click.option('--input-fp', required=True,
              type=click.Path(resolve_path=True, readable=True, exists=True,
                              file_okay=True),
              help='Filepath to input BIOM table')
@click.option('--output-fp', required=True,
              type=click.Path(resolve_path=True, readable=True, exists=False,
                              file_okay=True),
              help='Filepath to alpha diversity results')
@click.option('--tree-fp', required=True,
              type=click.Path(resolve_path=True, readable=True, exists=True,
                              file_okay=True),
              help='Filepath to tree')
@click.option('--diversity-metric', multiple=True,
              type=click.Choice(['chao1', 'faith_pd', 'shannon',
                                 'observed_otus']),
              help='Alpha diversity metric')
def main(input_fp,
         output_fp,
         tree_fp,
         diversity_metric):
    table = biom.load_table(input_fp)
    all_metrics = pd.Series()
    for metric in diversity_metric:
        kwargs = {}
        if metric == 'faith_pd':
            tree = skbio.TreeNode.read(tree_fp)
            otu_ids = table.ids(axis='observation')
            kwargs = {'tree': tree,
                      'otu_ids': otu_ids}
        result = compute_alpha_diversity(table, metric, **kwargs)
        if all_metrics.empty:
            all_metrics = result
        else:
            all_metrics = pd.concat([all_metrics, result], axis=1)
    all_metrics.to_csv(output_fp,
                       header=True,
                       index=True,
                       sep='\t')


if __name__ == "__main__":
    main()