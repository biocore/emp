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

"""Test suite for the most_wanted_otus.py module."""

from os import makedirs, getcwd, chdir
from os.path import exists, join
from shutil import rmtree
from tempfile import mkdtemp, NamedTemporaryFile
from cogent.app.formatdb import build_blast_db_from_fasta_path
from cogent.util.misc import remove_files
from cogent.util.unit_test import TestCase, main
from qiime.test import initiate_timeout, disable_timeout
from qiime.util import get_qiime_temp_dir, get_tmp_filename
from qiime.workflow import WorkflowError

from emp_isme14.new_diversity_places import generate_new_diversity_plots

class NewDiversityPlacesTests(TestCase):
    def setUp(self):
        """Set up files/environment that will be used by the tests."""
        # The prefix to use for temporary files. This prefix may be added to,
        # but all temp dirs and files created by the tests will have this
        # prefix at a minimum.
        self.prefix = 'new_diversity_places_tests_'
        self.files_to_remove = []
        self.dirs_to_remove = []

        self.output_dir = mkdtemp(prefix='%soutput_dir_' % self.prefix)
        self.dirs_to_remove.append(self.output_dir)

        self.otu_table1_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.biom')
        self.otu_table1_f.write(otu_table1)
        self.otu_table1_f.seek(0, 0)

        self.otu_table2_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.biom')
        self.otu_table2_f.write(otu_table2)
        self.otu_table2_f.seek(0, 0)

        self.ref_seqs_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.fasta')
        self.ref_seqs_f.write(ref_seqs)
        self.ref_seqs_f.seek(0, 0)

        self.mapping_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.txt')
        self.mapping_f.write(mapping)
        self.mapping_f.seek(0, 0)

#        self.ts_1_f = NamedTemporaryFile(prefix=self.prefix,
#                suffix='.txt')
#        self.ts_1_f.write(ts_1)
#        self.ts_1_f.seek(0, 0)

        self.mapping_category = 'Environment'

    def tearDown(self):
        """Remove temporary files/dirs."""
        remove_files(self.files_to_remove)
        # remove directories last, so we don't get errors
        # trying to remove files which may be in the directories
        for d in self.dirs_to_remove:
            if exists(d):
                rmtree(d)

    def test_generate_new_diversity_plots(self):
        exp = ([(28.846153846153843, 'Env1 (n=2)', [0.0, 57.692307692307686]),
            (57.142857142857139, 'Env2 (n=1)', [57.142857142857139])],
            [(2.0, 'Env1 (n=2)', [0, 4]), (3.0, 'Env2 (n=1)', [3])])
        obs = generate_new_diversity_plots(
                [self.otu_table1_f, self.otu_table2_f], self.ref_seqs_f,
                self.mapping_f, self.mapping_category, 1)

        self.assertEqual(len(obs[0]), len(exp[0]))
        self.assertFloatEqual(obs[0][0][:2], exp[0][0][:2])
        self.assertFloatEqual(sorted(obs[0][0][2]), sorted(exp[0][0][2]))
        self.assertFloatEqual(obs[0][1][:2], exp[0][1][:2])
        self.assertFloatEqual(sorted(obs[0][1][2]), sorted(exp[0][1][2]))

        self.assertEqual(len(obs[2]), len(exp[1]))
        self.assertFloatEqual(obs[2][0][:2], exp[1][0][:2])
        self.assertFloatEqual(sorted(obs[2][0][2]), sorted(exp[1][0][2]))

        self.assertFloatEqual(obs[2][1][:2], exp[1][1][:2])
        self.assertFloatEqual(sorted(obs[2][1][2]), sorted(exp[1][1][2]))

        ax = obs[1].get_axes()[0]
        self.assertEqual(ax.get_title(), "% Novel Seqs by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "% Novel Seqs")
        self.assertEqual(len(ax.get_xticklabels()), 2)

        ax = obs[3].get_axes()[0]
        self.assertEqual(ax.get_title(), "Number of Novel OTUs by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "Number of Novel OTUs")
        self.assertEqual(len(ax.get_xticklabels()), 2)

    def test_generate_new_diversity_plots_min_num_samples(self):
        exp = ([(28.846153846153843, 'Env1 (n=2)', [0.0, 57.692307692307686])],
               [(2.0, 'Env1 (n=2)', [0, 4])])
        obs = generate_new_diversity_plots(
                [self.otu_table1_f, self.otu_table2_f], self.ref_seqs_f,
                self.mapping_f, self.mapping_category, 2)

        self.assertEqual(len(obs[0]), len(exp[0]))
        self.assertFloatEqual(obs[0][0][:2], exp[0][0][:2])
        self.assertFloatEqual(sorted(obs[0][0][2]), sorted(exp[0][0][2]))

        self.assertEqual(len(obs[2]), len(exp[1]))
        self.assertFloatEqual(obs[2][0][:2], exp[1][0][:2])
        self.assertFloatEqual(sorted(obs[2][0][2]), sorted(exp[1][0][2]))

        ax = obs[1].get_axes()[0]
        self.assertEqual(ax.get_title(), "% Novel Seqs by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "% Novel Seqs")
        self.assertEqual(len(ax.get_xticklabels()), 1)

        ax = obs[3].get_axes()[0]
        self.assertEqual(ax.get_title(), "Number of Novel OTUs by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "Number of Novel OTUs")
        self.assertEqual(len(ax.get_xticklabels()), 1)

    def test_generate_new_diversity_plots_excluded_category_value(self):
        exp = ([(57.142857142857139, 'Env2 (n=1)', [57.142857142857139])],
               [(3.0, 'Env2 (n=1)', [3])])
        obs = generate_new_diversity_plots(
                [self.otu_table1_f, self.otu_table2_f], self.ref_seqs_f,
                self.mapping_f, self.mapping_category, 1, ['Env1'])

        self.assertFloatEqual(obs[0], exp[0])
        self.assertFloatEqual(obs[2], exp[1])

        ax = obs[1].get_axes()[0]
        self.assertEqual(ax.get_title(), "% Novel Seqs by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "% Novel Seqs")
        self.assertEqual(len(ax.get_xticklabels()), 1)

        ax = obs[3].get_axes()[0]
        self.assertEqual(ax.get_title(), "Number of Novel OTUs by Environment")
        self.assertEqual(ax.get_xlabel(), "Environment")
        self.assertEqual(ax.get_ylabel(), "Number of Novel OTUs")
        self.assertEqual(len(ax.get_xticklabels()), 1)


# Not sure if we'll need the following code...
#    def test_summarize_unclassified(self):
#        exp = 0.440363740522
#        obs = summarize_unclassified(self.ts_1_f)
#        self.assertFloatEqual(obs, exp)
#
#ts_1 = """
#Taxon	A	B
#Root;Other;Other;Other;Other;Other	5.07172689765e-06	0.28
#Root;k__Bacteria;Other;Other;Other;Other	0.0209081941356	0.123
#Root;k__Bacteria;p__Actinobacteria;c__Actinobacteria;Other;Other	1.5215180693e-05	0.456799
#Root;k__Bacteria;p__Firmicutes;c__Bacilli;o__Lactobacillales;f__Lactobacillaceae	0.00374800617736	0.14201
#"""

otu_table1 = """
{"rows": [{"id": "GG1", "metadata": null}, {"id": "New2", "metadata": null}, {"id": "GG2", "metadata": null}, {"id": "New1", "metadata": null}], "format": "Biological Observation Matrix 1.0.0", "data": [[0, 0, 1.0], [0, 1, 5.0], [1, 1, 1.0], [2, 0, 10.0], [3, 1, 3.0]], "columns": [{"id": "A", "metadata": null}, {"id": "B", "metadata": null}], "generated_by": "BIOM-Format 1.0.0c", "matrix_type": "sparse", "shape": [4, 2], "format_url": "http://biom-format.org", "date": "2012-08-10T10:36:36.386189", "type": "OTU table", "id": null, "matrix_element_type": "float"}
"""

otu_table2 = """
{"rows": [{"id": "GG3", "metadata": null}, {"id": "GG1", "metadata": null}, {"id": "New1", "metadata": null}, {"id": "New3", "metadata": null}, {"id": "New4", "metadata": null}], "format": "Biological Observation Matrix 1.0.0", "data": [[0, 0, 4.0], [0, 1, 3.0], [1, 0, 2.0], [2, 0, 7.0], [2, 1, 1.0], [3, 0, 3.0], [3, 1, 2.0], [4, 0, 1.0], [4, 1, 1.0]], "columns": [{"id": "B", "metadata": null}, {"id": "C", "metadata": null}], "generated_by": "BIOM-Format 1.0.0c", "matrix_type": "sparse", "shape": [5, 2], "format_url": "http://biom-format.org", "date": "2012-08-10T10:38:44.625396", "type": "OTU table", "id": null, "matrix_element_type": "float"}
"""

mapping = """
#SampleID	BarcodeSequence	LinkerPrimerSequence	Environment	Description
A	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env1	A_Env1
B	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env1	B_Env1
C	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env2	C_Env2
"""

ref_seqs = """
>GG1
ACGCTGGCGGCAGGCCTAACACATGCAAGTCGAGCGGCAGCGGAAAGTAGCTTGCTACTTTGCCGGCGAGCGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCTGATGGAGGGGGATAACTACTGGAAACGGTGGCTAATACCGCGTAACGTCGCAAGACCAAAGAGGGGGACCTTCGGGCCTCTCGCCATCAGATGTGCCCAGATGGGATTAGCTAGTAGGTGGGGTAATGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGATGACCAGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGGGAAACCCTGATGCAGCCATGCCGCGTGTGTGAAGAAGGCCTTAGGGTTGTAAAGCACTTTCAGCGGGGAGGAAGGGTAGGTACTTAATACGTGCTTACATTGACGTTACCCGCAGAAGAAGCACCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTTTGTTAAGTTAGATGTGAAATCCCCGGGCTTAACCTGGGAACTGCATTTAAAACTGGCAAGCTAGAGTCTTGTAGAGGGGGGTAGAATTCCATGTGTAGCGGTGAAATGCGTAGAGATGTGGAAGAATACCGGTGGCGAAGGCGGCCCCCTGGACAAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCTGTAAACGATGTCGACTTGGAGGTTGTTCCCTTGAGGAGTGGCTTCCGGAGCTAACGCGTTAAGTCGACCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAATGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCTACTCTTGACATCCAGAGAACTTAGCAGAGATGCTTTGGTGCCTTCGGGAACTCTGAGACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTTGTGAAATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTTATCCTTTGTTGCCAGCAAGTCATGTTGGGAACTCAAAGGAGACTGCCGGTGATAAACCGGAGGAAGGTGGGGATGACGTCAAGTCATCATGGCCCTTACGAGTAGGGCTACACACGTGCTACAATGGCGTATACAAAGAGAAGCTAACTCGCGAGAGCATGCGGACCTCATAAAGTACGTCGTAGTCCGGATCGGAGTCTGCAACTCGACTCCGTGAAGTCGGAATCGCTAGTAATCGTGGATCAGAATGCCACGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGTGGGTTGCAAAAGAAGTAGGTAGCTTAACCTTCGGGAGGGCGCTTACCACTTTGTGATTCATGACTGGGGTGAAGTCGTAACAAGGTAACCGTAGGG
>GG2
TTGATCCTGGCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAACAGGAAGGAGCTTGCTTCTTTGCTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGGATCTGCCTGATGGAGGGGGATAACTACTGGAAACGGTAGCTAATACCGCATAATGTCGCGAGACCAAAGCGGGGGACCTTCGGGCCTCGCACCATCAGATGAACCCAGATGGGATTAGCTAGCAGGTAGGGTAATGGCCTACCTGGGCGACGATCCCTAGCTGGTNTGAGAGGATGACCAGCCACACTGGAACTGAGACACGGTCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGCGCAAGCCTGATGCTGCCATGCCGCGTGTATGAAGAAGGCCTTAGGGTTGTAAAGTACTTTCAGTCAGGAGGAAGGCGTGAGTGTTAATATCACTTGCGATTGACGTTACTGACAGAAGAAGCACCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTCTGTTAAGTCAGATGTGAAATCCCCGGGCTCAACCTGGGAACTGCATTTGAAACTGGCAGACTTGAGTCTTGTAGAGGGGGGTAGAATTCCAGGTGTAGCGGTGAAATGCGTAGAGATCTGGAGGAATACCGGTGGCGAAGGCGGCCCCCTGGACAAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGTCGACTTGGAGGTTGTTCCCTTGAGGAGTGGCTTCCGGANNTAACGCGTTAAGTCGANNGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAATGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCTACTCTTGACATCCAGAGAACCGAGCAGAGATGCTTGGGTGCCTTCGGGAACTCTGAGACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTTGTGAAATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTTATCCTTTGTTGCCAGCGATTCGGTCGGGAACTCAAAGGAGACTGCCGGTGATAAACCGGAGGAAGGTGGGGATGACGTCAAGTCATCATGGCCCTTACGAGTAGGGCTACACACGTGCTACAATGGCGCATACAAAGAGAAGCGACCTCGCGAGAGCAAGCGGACCTCATAAAGTGCGTCGTAGTCCGGATTGGAGTCTGCAACTCGACTCCATGAAGTCGGAATCGCTAGTAATCGTGAATCAGAATGTCACGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGTGGGTTGCAAAAGAAGTAGATAGCTTAACCTTCGGGAGGGCGTTTACCACTTTGTGATTCATGACTGGGGTGAAGTCGTAACAAGGTAACCGTAGGGGAACCTGCGGCTGGATCA
>GG4
AGAGTTTGATCCTGGCTCAGGATGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAACGAAGCACTTTATTTGATTTCCTCCGGGGATGAAGATTTTGTGACTGAGTGGCGGACGGGTGAGTAACGCGTGGGCAACCTGCCCCATACCGGGGGATAACAGCTGGAAACGGCTGCTAATACCGCATAAGCGCACAGTGCTGCATGGCACGGTGTGAAAAACTCCGGTGGTATGGGATGGACCCGCGTCTGATTAGCCAGTTGGCAGGGTAACGGCCTACCAAAGCGACGATCAGTAGCCGACCTGAGAGGGTGACCGGCCACATTGGGACTGAGACACGGCCCAAACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGGGAAACCCTGATGCAGCGACGCCGCGTGAGCGAAGAAGTATTTCGGTATGTAAAGCTCTATCAGCAGGGAAGAAGAATGACGGTACCTGACTAAGAAGCACCGGCTAAATACGTGCCAGCAGCCGCGGTAATACGTATGGTGCAAGCGTTATCCGGATTTACTGGGTGTAAAGGGAGCGCAGGCGGTACGGCAAGTCTGATGTGAAAGTCCGGGGCTCAACCCCGGTACTGCATTGGAAACTGTCGGACTAGAGTGTCGGAGGGGTAAGTGGAATTCCTAGTGTAGCGGTGAAATGCGTAGATATTAGGAGGAACACCAGTGGCGAAGGCGGCTTACTGGACGATCACTGACGCTGAGGCTCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGAATACTAGGTGTCGGGAGGCATTGCCTTTCGGTGCCGCCGCAAACGCATTAAGTATTCCACCTGGGGAGTACGTTCGCAAGAATGAAACTCAAAGGAATTGACGGGGACCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGAAGCAACGCGAAGAACCTTACCAAGTCTTGACATCCCGGTGACAGAGTATGTAATGTGCTTTCCTTTCGGGGCACCGGAGACAGGTGGTGCATGGTTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCCTGTCCTTAGTAGCCAGCAGTAAGATGGGCACTCTAGGGAGACTGCCAGGGATAACCTGGAGGAAGGCGGGGATGACGTCAAATCATCATGCCCCTTATGACTTGGGCTACACACGTGCTACAATGGCGTAAACAAAGGGAAGCGAGCCTGTGAGGGGGAGCAAATCCCAAAAATAACGTCTCAGTTCGGACTGTAGTCTGCAACCCGACTACACGAAGCTGGAATCGCTAGTAATCGCGAATCAGAATGTCGCGGTGAATACGTTCCCGGGTCTTGTACACACCGCCCGTCACACCATGGGAGTTGGAAATGCCCGAAGTCAGTGACCCAACCGCAAGGAGGGAGCTGCCGAAGGCAGGTTCGATAACTGGG
>GG3
CCGGACCCGACCGCTATCGGGGTGGGGCTAAGCCATGGGAGTCGCACGCTCCGCCGCTGCGGGGCGTGGCGCACGGCTGAGTAGCACGTGGCTAACCTGCCCTCGGGAGGGGGATAACACCGGGAAACTGGTGCTAATCCCCCATAGGGGAAGGCGCCTGGAAGGGTCCTTCCTCGAAAAGGCCCGGCAGGGGTTAGCGCTGCCGAGCCGCCCGAGGATGGGGCTACGGCCCATCAGGTAGTTGGCGGGGTAACGGCCCGCCAAGCCGATAACGGGTGGGGGCCGTGAGAGCGGGAGCCCCCAGATGGGCACTGAGACAAGGGCCCAGGCCCTAAGGGGCGCACCAGGCGCGAAACCTCCGCAATGCNGGAAACCGTGACGGGGCCACCCCGAGTGCCCCCTTTCCGGGGGCTTTTCCCCGCTGTAGGAAGGCGGGGGAATAAGCGGGGGGCAAGTCTGGTGTCAGCCGCCGCCGTAATACCAGCCCCGCGAGTGGTCGGGACGGTTATTGGGCCTAAAGCGCCCGTAGCCGGCCCGGCAAGTCCCCTCCTAAATCCCCGGGCTCAACCTGGGGACTGGGGGGGATACTGCCGGGCTAGGGGGCGGGAGAGGCCGAGGGTACTCCCGGGGTAGGGGCGAAATCCTATAATCCCGGGAGGACCACCAGTGGCGAAGGCGCTCGGCTGGAACGCGCCCGACGGTGAGGGGCGAAAGCCGGGGGAGCAAACCGGATTAGATACCGGGTAGTCCCGGCTGTAAACGATGCGGGCTAGCTGTTGGGTGGGCTTAGAGCCCACCCAGTGGCGCAGGGAAGCCGTTAAGCCCGCCGCCTGGGGAGTACGGCCGCAAGGCTGAAACTTAAAGGAATTGGCGGGGGAGCACCACAAGGGGTGGAGCCTGCGGTTCAATTGGAGTCAACGCCGGGAATCTCACCGGGGGCGACAGCAGGATGACGGCCAGGCTAACGACCTTGCCTGACGCGCTGAGAGGAGGTGCATGGCCGTCGCCAGCTCGTGCCGTGAGGTGTCCGGTTAAGTCCGGAAACGAGCGAGACCCCTGNCCCCAGTTGCGANNNNNNNCTACGGCCCTGGGGCACACTGGGGGGACTGCCGCCGTTCAAGGCGGAGGAAGGAGGGGGCCACGGCAGGTCAGCATGCCCCGAATCCCCCGGGCTACACGCGGGCTACAATGGCGGGGACAGCGGGTTCCGACCCCGAAAGGGGGAGGCAATCCCTCAAACCCCGCCGCAGTTGGGATCGAGGGCTGCAACTCGCCCTCGTGAACGCGGAATCCCTAGTAACCGCGCGTCAACATCGCGCGGTGAATACGTCCCTGCTCCTTGCACACACCGCCCGTCGCTCCACCCGAGGGGAGAGGGAGTGAGGCCTGGCCGGCTTGGTCGGGTCGAACTCCCTCTCCCTGAGGGGGGAGA
"""


if __name__ == "__main__":
    main()
