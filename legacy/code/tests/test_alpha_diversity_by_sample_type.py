#!/usr/bin/env python
from __future__ import division

__author__ = "Jai Ram Rideout"
__copyright__ = "Copyright 2012, The QIIME project"
__credits__ = ["Jai Ram Rideout"]
__license__ = "GPL"
__version__ = "1.5.0-dev"
__maintainer__ = "Jai Ram Rideout"
__email__ = "jai.rideout@gmail.com"
__status__ = "Development"

from os import makedirs, getcwd, chdir
from os.path import exists, join
from shutil import rmtree
from tempfile import mkdtemp, NamedTemporaryFile
from cogent.app.formatdb import build_blast_db_from_fasta_path
from cogent.util.misc import remove_files
from cogent.util.unit_test import TestCase, main
from qiime.test import initiate_timeout, disable_timeout
from qiime.util import get_qiime_temp_dir, get_tmp_filename
from qiime.workflow.util import WorkflowError

from emp.alpha_diversity_by_sample_type import (
        alpha_diversity_by_sample_type)

class AlphaDiversityBySampleTypeTests(TestCase):
    def setUp(self):
        """Set up files/environment that will be used by the tests."""
        # The prefix to use for temporary files. This prefix may be added to,
        # but all temp dirs and files created by the tests will have this
        # prefix at a minimum.
        self.prefix = 'alpha_diversity_by_sample_type_tests_'
        self.files_to_remove = []
        self.dirs_to_remove = []

        self.adiv_1_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.txt')
        self.adiv_1_f.write(adiv_1)
        self.adiv_1_f.seek(0, 0)

        self.adiv_2_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.txt')
        self.adiv_2_f.write(adiv_2)
        self.adiv_2_f.seek(0, 0)

        self.adiv_fs = [self.adiv_1_f, self.adiv_2_f]

        self.mapping_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.txt')
        self.mapping_f.write(mapping)
        self.mapping_f.seek(0, 0)

        self.mapping_category = 'Environment'

    def tearDown(self):
        """Remove temporary files/dirs."""
        remove_files(self.files_to_remove)
        # remove directories last, so we don't get errors
        # trying to remove files which may be in the directories
        for d in self.dirs_to_remove:
            if exists(d):
                rmtree(d)

    def test_alpha_diversity_by_sample_type(self):
        """Functions correctly using standard valid input data."""
        exp = [(2.0, 'Env2 (n=3)', [5.0, 2.0, 2.0]),
               (4.0, 'Env1 (n=5)', [7.0, 4.0, 0.0, 1.0, 9.0])]
        obs = alpha_diversity_by_sample_type(self.adiv_fs, self.mapping_f,
                                             self.mapping_category, 2)
        self.assertFloatEqual(obs[0], exp)

        ax = obs[1].get_axes()[0]
        self.assertEqual(ax.get_title(), "Alpha Diversity by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "Alpha Diversity")
        self.assertEqual(len(ax.get_xticklabels()), 2)

    def test_alpha_diversity_by_sample_type_min_num_samples(self):
        exp = [(4.0, 'Env1 (n=5)', [7.0, 4.0, 0.0, 1.0, 9.0])]
        obs = alpha_diversity_by_sample_type(self.adiv_fs, self.mapping_f,
                                             self.mapping_category, 4)
        self.assertFloatEqual(obs[0], exp)

        ax = obs[1].get_axes()[0]
        self.assertEqual(ax.get_title(), "Alpha Diversity by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "Alpha Diversity")
        self.assertEqual(len(ax.get_xticklabels()), 1)

    def test_alpha_diversity_by_sample_type_excluded_category_value(self):
        exp = [(2.0, 'Env2 (n=3)', [5.0, 2.0, 2.0])]
        obs = alpha_diversity_by_sample_type(self.adiv_fs, self.mapping_f,
                                             self.mapping_category, 2,
                                             ['Env1'])
        self.assertFloatEqual(obs[0], exp)

        ax = obs[1].get_axes()[0]
        self.assertEqual(ax.get_title(), "Alpha Diversity by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "Alpha Diversity")
        self.assertEqual(len(ax.get_xticklabels()), 1)


adiv_1 = """
	observed_species
S1	7
S2	5
S3	4
S4	0
"""

adiv_2 = """
	observed_species
S4	1
S5	2
S6	2
S7	9
"""

mapping = """
#SampleID	BarcodeSequence	LinkerPrimerSequence	Environment	Description
S1	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env1	foo
S2	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env2	bar
S3	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env1	baz
S4	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env1	bazz
S5	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env2	bazz
S6	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env2	bazz
S7	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env1	bazz
"""


if __name__ == "__main__":
    main()
