#!/usr/bin/env python
from __future__ import division

__author__ = "Jai Ram Rideout"
__copyright__ = "Copyright 2013, The QIIME Project"
__credits__ = ["Jai Ram Rideout"]
__license__ = "GPL"
__version__ = "1.7.0-dev"
__maintainer__ = "Jai Ram Rideout"
__email__ = "jai.rideout@gmail.com"
__status__ = "Development"

"""Contains functions used in the novel_samples.py script."""

from collections import defaultdict
from operator import itemgetter

from biom.parse import parse_biom_table

from cogent.parse.fasta import MinimalFastaParser

def compute_sample_novelty(table_fs, rep_set_f, verbose=False):
    """"""
    ref_otus = [seq_id.split()[0] for seq_id, _ in
                MinimalFastaParser(rep_set_f)]

    # {sample_id: [novel_count, known_count, [novel_obs_ids]]}
    sample_novelty = defaultdict(lambda: [0, 0, []])
    tables_processed = 0
    for table_f in table_fs:
        table = parse_biom_table(table_f)
        novel_obs = set(table.ObservationIds) - set(ref_otus)

        for counts, obs_id, _ in table.iterObservations():
            if obs_id in novel_obs:
                for sid, count in zip(table.SampleIds, counts):
                    if count > 0:
                        sample_novelty[sid][0] += count
                        sample_novelty[sid][2].append(obs_id)
            else:
                for sid, count in zip(table.SampleIds, counts):
                    sample_novelty[sid][1] += count

        tables_processed += 1
        if verbose:
            print "Processed %d table(s)." % tables_processed

    results = []
    for sid, (novel_count, known_count, novel_obs_ids) in \
            sample_novelty.items():
        percent_novel_seqs = (novel_count / (known_count + novel_count)) * 100

        # Create a set first in case a sample in multiple tables has the same
        # novel observations.
        num_new_obs = len(set(novel_obs_ids))
        results.append((sid, num_new_obs, percent_novel_seqs))

    return sorted(results, reverse=True, key=itemgetter(1))
