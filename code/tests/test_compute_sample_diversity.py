#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Evguenia Kopylova.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from unittest import TestCase, main
from tempfile import mkstemp, mkdtemp
from os import close
from shutil import rmtree

from compute_sample_diversity import (union, intersect, sample_ids,
                                      get_metrics, compute_outliers)


# Test class and cases
class ComputeSampleDiversity(TestCase):
    """ Tests for compute_sample_diversity.py functionality """

    def setUp(self):
        """ Create temporary seqs file
        """
        self.root_dir = mkdtemp()
        # create alpha diversity 1
        f, self.alpha_1_fp = mkstemp(prefix='alpha_1_',
                                     suffix='.txt')
        close(f)

        # write alpha diversity 1 to file
        with open(self.alpha_1_fp, 'w') as tmp:
            tmp.write(alpha_1)

        # create alpha diversity 2
        f, self.alpha_2_fp = mkstemp(prefix='alpha_2_',
                                     suffix='.txt')
        close(f)

        # write alpha diversity 1 to file
        with open(self.alpha_2_fp, 'w') as tmp:
            tmp.write(alpha_2)

    def tearDown(self):
        rmtree(self.root_dir)

    def test_union(self):
        """Test union() function.
        """
        l1 = ['s1', 's2', 's3', 's5', 's7']
        l2 = ['s1', 's2', 's5', 's7', 's9', 's10']
        exp_union = sorted(['s1', 's2', 's3', 's5', 's7', 's9', 's10'])
        act_union = sorted(union(l1, l2))
        self.assertListEqual(exp_union, act_union)

    def test_intersect(self):
        """Test intersect() function.
        """
        l1 = ['s1', 's2', 's3', 's7', 's9', 's10']
        l2 = ['s2', 's3', 's4', 's10']
        exp_intersect = sorted(['s2', 's3', 's10'])
        act_intersect = sorted(intersect(l1, l2))
        self.assertListEqual(exp_intersect, act_intersect)

    def test_sample_ids(self):
        """Test sample_ids() function.
        """
        exp_list = sorted(['s1', 's2', 's3', 's6', 's7', 's4', 's5'])
        act_list = sorted(sample_ids(self.alpha_1_fp))
        self.assertListEqual(exp_list, act_list)

    def test_get_metrics(self):
        """Test get_metrics() function.
        """
        all_sample_ids = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
        metric = "PD_whole_tree"
        exp_metrics = [('s1', '163.66'), ('s2', '255.61'),
                       ('s3', '405.26'), ('s4', '218.99'),
                       ('s5', '193.49'), ('s6', '202.58'),
                       ('s7', '125.10')]
        act_metrics = get_metrics(self.alpha_2_fp, all_sample_ids, metric)
        self.assertEqual(len(exp_metrics), len(act_metrics))
        for m in exp_metrics:
            self.assertTrue(m in act_metrics)

    def test_compute_outliers(self):
        """Test compute_outliers() function.
        """
        metric_a = [('s1', '163.66'), ('s2', '255.61'),
                    ('s3', '405.26'), ('s4', '218.99'),
                    ('s5', '193.49'), ('s6', '202.58'),
                    ('s7', '125.10')]
        metric_b = [('s1', '87.58'), ('s2', '142.89'),
                    ('s3', '223.69'), ('s4', '120.16'),
                    ('s5', '106.40'), ('s6', '110.35'),
                    ('s7', '61.81')]
        offset = 1.5
        outliers_exp = ['s3']
        outliers_act = sorted(compute_outliers(metric_a, metric_b, offset))
        self.assertListEqual(outliers_exp, outliers_act)


alpha_1 = """\tPD_whole_tree\tchao1\tobserved_otus\tshannon
s1\t87.58\t1768.04\t1500.0\t5.47
s2\t142.89\t3286.65\t2573.0\t5.55
s3\t223.69\t6016.00\t4366.0\t6.70
s4\t120.16\t2680.66\t2017.0\t6.51
s5\t106.40\t2213.84\t1816.0\t5.52
s6\t110.35\t2386.24\t1849.0\t6.34
s7\t61.81\t1593.5\t1075.0\t5.74
"""

alpha_2 = """\tPD_whole_tree\tchao1\tobserved_otus\tshannon
s1\t163.66\t2612.34\t2111.0\t5.77
s2\t255.61\t4403.90\t3398.0\t5.63
s3\t405.26\t8072.96\t5600.0\t6.92
s7\t125.10\t2322.13\t1596.0\t5.94
s6\t202.58\t3252.58\t2535.0\t6.55
s5\t193.49\t3128.37\t2461.0\t5.67
s4\t218.99\t3803.95\t2750.0\t6.72
"""

if __name__ == '__main__':
    main()
