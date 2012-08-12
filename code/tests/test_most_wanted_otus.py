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

from emp_isme14.most_wanted_otus import (generate_most_wanted_list,
        _get_most_wanted_filtering_commands, _get_top_n_blast_results,
        _get_rep_set_lookup)

class MostWantedOtusTests(TestCase):
    """Tests for the most_wanted_otus.py module."""

    def setUp(self):
        """Set up files/environment that will be used by the tests."""
        # The prefix to use for temporary files. This prefix may be added to,
        # but all temp dirs and files created by the tests will have this
        # prefix at a minimum.
        self.prefix = 'most_wanted_otus_tests_'
        self.files_to_remove = []
        self.dirs_to_remove = []

        self.output_dir = mkdtemp(prefix='%soutput_dir_' % self.prefix)
        self.dirs_to_remove.append(self.output_dir)

        self.otu_table_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.biom')
        self.otu_table_f.write(otu_table)
        self.otu_table_f.seek(0, 0)

        self.rep_set_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.fasta')
        self.rep_set_f.write(rep_set)
        self.rep_set_f.seek(0, 0)

        self.ref_seqs_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.fasta')
        self.ref_seqs_f.write(ref_seqs)
        self.ref_seqs_f.seek(0, 0)

        self.mapping_f = NamedTemporaryFile(prefix=self.prefix,
                suffix='.txt')
        self.mapping_f.write(mapping)
        self.mapping_f.seek(0, 0)

        self.grouping_category = 'Environment'
        self.top_n = 100

        self.blast_results_lines = blast_results.split('\n')
        self.rep_set_lines = rep_set.split('\n')

    def tearDown(self):
        """Remove temporary files/dirs."""
        remove_files(self.files_to_remove)
        # remove directories last, so we don't get errors
        # trying to remove files which may be in the directories
        for d in self.dirs_to_remove:
            if exists(d):
                rmtree(d)

    def test_generate_most_wanted_list(self):
        """Functions correctly using standard valid input data."""
        generate_most_wanted_list(self.otu_table_f.name, self.rep_set_f.name,
                self.ref_seqs_f.name, self.mapping_f.name,
                self.grouping_category, self.output_dir, self.top_n)
        obs_txt_f = open(join(self.output_dir,
                              'top_%d_most_wanted_otus.txt' % self.top_n), 'U')
        obs_txt = obs_txt_f.read()
        obs_txt_f.close()
        self.assertEqual(obs_txt, exp_txt)

    def test_generate_new_otus_stats(self):
        """Test generating new OTU stats on valid input data."""
        exp = [('New.CleanUp.ReferenceOTU972',
            'ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGGGTGCGTAGGCGGATGTTTAAG'
            'TGGGATGTGAAATCCCCGGGCTTAACCTGGGGGCTGC', 'foo;bar;baz', 2, 60.0,
            4.349999999999994, {'Env2': 25.0, 'Env1': 35.0}),
            ('New.CleanUp.ReferenceOTU969',
            'ATACGTAGGTCCCGAGCGTTGTCCGGATTTACTGGGTGTAAAGGGAGCGTAGACGGCATGGCAAG'
            'TCTGAAGTGAAAACCCAGGGCTCAACCCTGGGACTGC', 'foo;bar;baz', 2, 14.0,
            12.5, {'Env2': 8.0, 'Env1': 6.0}), ('New.CleanUp.ReferenceOTU964',
            'ATACGGAGGATGCGAGCGTTATCCGGATTTATTGGGTTTAAAGGGTGCGTAGACGGCGAAGCAAG'
            'TCTGAAGTGAAAGCCCGGGGCTCAACCGCGGGACTGC', 'foo;bar;baz', 2, 5.0,
            14.769999999999996, {'Env2': 2.0, 'Env1': 3.0}),
            ('New.CleanUp.ReferenceOTU999',
            'ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGGGTGCGTAGGCGGATGTTTAAG'
            'TGGGATGTGAAATCCCCGGGCTTAACCTGGGGGCTGC', 'foo;bar;bazz', 1, 99.0,
            4.349999999999994, {'Env2': 0.0, 'Env1': 99.0})]

        ref_seqs_db, ref_seqs_db_files_to_remove = \
            build_blast_db_from_fasta_path(self.ref_seqs_f.name)
        obs = _generate_new_otus_stats(self.otu_table_f, self.rep_set_f,
                self.ref_seqs_f, ref_seqs_db, self.mapping_f,
                self.grouping_category, self.top_n)
        remove_files(ref_seqs_db_files_to_remove)

        self.assertFloatEqual(obs, exp)

    def test_get_most_wanted_filtering_commands(self):
        obs = _get_most_wanted_filtering_commands('/foo', ['/a.biom',
                '/b.biom', '/c.biom'], '/rs.fna', '/gg.fasta', '/nt',
                '/map.txt', 'Env', 30, 100, 5, 0.70, 1e-4, 25, 55)
        self.assertEqual(obs, exp_commands)

    def test_get_top_n_blast_results(self):
        exp = [('New.CleanUp.ReferenceOTU969', 'gi|16|emb|Z52700.1|', 90.0),
                ('New.CleanUp.ReferenceOTU999', 'gi|7|emb|X51700.1|', 100.0),
                ('New.CleanUp.ReferenceOTU972', 'gi|7|emb|T51700.1|', 100.0)]
        obs = _get_top_n_blast_results(self.blast_results_lines, self.top_n)
        self.assertFloatEqual(obs, exp)

    def test_get_rep_set_lookup(self):
        obs = _get_rep_set_lookup(self.rep_set_lines)
        self.assertEqual(obs, exp_rep_set_lookup)


otu_table = """
{"rows": [{"id": "10115", "metadata": {"taxonomy": "foo;bar;baz"}}, {"id": "10113", "metadata": {"taxonomy": "foo;bar;baz"}}, {"id": "102506", "metadata": {"taxonomy": "foo;bar;baz"}}, {"id": "New.CleanUp.ReferenceOTU964", "metadata": {"taxonomy": "foo;bar;baz"}}, {"id": "New.CleanUp.ReferenceOTU969", "metadata": {"taxonomy": "foo;bar;baz"}}, {"id": "New.CleanUp.ReferenceOTU972", "metadata": {"taxonomy": "foo;bar;baz"}}, {"id": "New.CleanUp.ReferenceOTU999", "metadata": {"taxonomy": "foo;bar;bazz"}}], "format": "Biological Observation Matrix 1.0.0", "data": [[0, 0, 6.0], [1, 0, 18.0], [2, 0, 6.0], [3, 0, 3.0], [4, 0, 6.0], [5, 0, 35.0], [6, 0, 99.0], [0, 1, 0.0], [1, 1, 1.0], [2, 1, 5.0], [3, 1, 2.0], [4, 1, 8.0], [5, 1, 25.0], [6, 1, 0.0]], "columns": [{"id": "S1", "metadata": null}, {"id": "S2", "metadata": null}], "generated_by": "QIIME 1.5.0-dev, svn revision 3175", "matrix_type": "sparse", "shape": [7, 2], "format_url": "http://biom-format.org", "date": "2012-08-06T16:56:21.226213", "type": "OTU table", "id": null, "matrix_element_type": "float"}
"""

rep_set = """
>New.CleanUp.ReferenceOTU999 S1_18210
ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGGGTGCGTAGGCGGATGTTTAAGTGGGATGTGAAATCCCCGGGCTTAACCTGGGGGCTGC
>10113 S1_88960
ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTCTGTTAAGTCAGATGTGAAATCCCCGGGCTCCACCTGGGCACTGC
>10115 S2_9552
ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTTTGTTAAGTTTGATGTGAAATCCCCGGGCTTAACCTGGGAACTGC
>102506 S1_46428
ATACGTATGGTGCAAGCGTTATCCGGATTTACTGGGTGTAAAGGGAGCGCAGGCGGTACGGCAAGTCTGATGTGAAAGTCCGGGGCTCAACCCCGGTACTGC
AAACGTAGGGTGCAAGCGTTGTCCGGAATTACTGGGTGTAAAGGGAGCGTAGACGGCTGTGCAAGTCTGAAGTGAAAGGCATGGGCTCAACCTGTGGACTGC
>New.CleanUp.ReferenceOTU964 S2_295794
ATACGGAGGATGCGAGCGTTATCCGGATTTATTGGGTTTAAAGGGTGCGTAGACGGCGAAGCAAGTCTGAAGTGAAAGCCCGGGGCTCAACCGCGGGACTGC
>New.CleanUp.ReferenceOTU969 S2_166346
ATACGTAGGTCCCGAGCGTTGTCCGGATTTACTGGGTGTAAAGGGAGCGTAGACGGCATGGCAAGTCTGAAGTGAAAACCCAGGGCTCAACCCTGGGACTGC
>New.CleanUp.ReferenceOTU972 S1_18219
ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGGGTGCGTAGGCGGATGTTTAAGTGGGATGTGAAATCCCCGGGCTTAACCTGGGGGCTGC
"""

ref_seqs = """
>10115
ACGCTGGCGGCAGGCCTAACACATGCAAGTCGAGCGGCAGCGGAAAGTAGCTTGCTACTTTGCCGGCGAGCGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCTGATGGAGGGGGATAACTACTGGAAACGGTGGCTAATACCGCGTAACGTCGCAAGACCAAAGAGGGGGACCTTCGGGCCTCTCGCCATCAGATGTGCCCAGATGGGATTAGCTAGTAGGTGGGGTAATGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGATGACCAGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGGGAAACCCTGATGCAGCCATGCCGCGTGTGTGAAGAAGGCCTTAGGGTTGTAAAGCACTTTCAGCGGGGAGGAAGGGTAGGTACTTAATACGTGCTTACATTGACGTTACCCGCAGAAGAAGCACCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTTTGTTAAGTTAGATGTGAAATCCCCGGGCTTAACCTGGGAACTGCATTTAAAACTGGCAAGCTAGAGTCTTGTAGAGGGGGGTAGAATTCCATGTGTAGCGGTGAAATGCGTAGAGATGTGGAAGAATACCGGTGGCGAAGGCGGCCCCCTGGACAAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCTGTAAACGATGTCGACTTGGAGGTTGTTCCCTTGAGGAGTGGCTTCCGGAGCTAACGCGTTAAGTCGACCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAATGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCTACTCTTGACATCCAGAGAACTTAGCAGAGATGCTTTGGTGCCTTCGGGAACTCTGAGACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTTGTGAAATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTTATCCTTTGTTGCCAGCAAGTCATGTTGGGAACTCAAAGGAGACTGCCGGTGATAAACCGGAGGAAGGTGGGGATGACGTCAAGTCATCATGGCCCTTACGAGTAGGGCTACACACGTGCTACAATGGCGTATACAAAGAGAAGCTAACTCGCGAGAGCATGCGGACCTCATAAAGTACGTCGTAGTCCGGATCGGAGTCTGCAACTCGACTCCGTGAAGTCGGAATCGCTAGTAATCGTGGATCAGAATGCCACGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGTGGGTTGCAAAAGAAGTAGGTAGCTTAACCTTCGGGAGGGCGCTTACCACTTTGTGATTCATGACTGGGGTGAAGTCGTAACAAGGTAACCGTAGGG
>10113
TTGATCCTGGCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAACAGGAAGGAGCTTGCTTCTTTGCTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGGATCTGCCTGATGGAGGGGGATAACTACTGGAAACGGTAGCTAATACCGCATAATGTCGCGAGACCAAAGCGGGGGACCTTCGGGCCTCGCACCATCAGATGAACCCAGATGGGATTAGCTAGCAGGTAGGGTAATGGCCTACCTGGGCGACGATCCCTAGCTGGTNTGAGAGGATGACCAGCCACACTGGAACTGAGACACGGTCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGCGCAAGCCTGATGCTGCCATGCCGCGTGTATGAAGAAGGCCTTAGGGTTGTAAAGTACTTTCAGTCAGGAGGAAGGCGTGAGTGTTAATATCACTTGCGATTGACGTTACTGACAGAAGAAGCACCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTCTGTTAAGTCAGATGTGAAATCCCCGGGCTCAACCTGGGAACTGCATTTGAAACTGGCAGACTTGAGTCTTGTAGAGGGGGGTAGAATTCCAGGTGTAGCGGTGAAATGCGTAGAGATCTGGAGGAATACCGGTGGCGAAGGCGGCCCCCTGGACAAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGTCGACTTGGAGGTTGTTCCCTTGAGGAGTGGCTTCCGGANNTAACGCGTTAAGTCGANNGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAATGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCTACTCTTGACATCCAGAGAACCGAGCAGAGATGCTTGGGTGCCTTCGGGAACTCTGAGACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTTGTGAAATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTTATCCTTTGTTGCCAGCGATTCGGTCGGGAACTCAAAGGAGACTGCCGGTGATAAACCGGAGGAAGGTGGGGATGACGTCAAGTCATCATGGCCCTTACGAGTAGGGCTACACACGTGCTACAATGGCGCATACAAAGAGAAGCGACCTCGCGAGAGCAAGCGGACCTCATAAAGTGCGTCGTAGTCCGGATTGGAGTCTGCAACTCGACTCCATGAAGTCGGAATCGCTAGTAATCGTGAATCAGAATGTCACGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGTGGGTTGCAAAAGAAGTAGATAGCTTAACCTTCGGGAGGGCGTTTACCACTTTGTGATTCATGACTGGGGTGAAGTCGTAACAAGGTAACCGTAGGGGAACCTGCGGCTGGATCA
>102506
AGAGTTTGATCCTGGCTCAGGATGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAACGAAGCACTTTATTTGATTTCCTCCGGGGATGAAGATTTTGTGACTGAGTGGCGGACGGGTGAGTAACGCGTGGGCAACCTGCCCCATACCGGGGGATAACAGCTGGAAACGGCTGCTAATACCGCATAAGCGCACAGTGCTGCATGGCACGGTGTGAAAAACTCCGGTGGTATGGGATGGACCCGCGTCTGATTAGCCAGTTGGCAGGGTAACGGCCTACCAAAGCGACGATCAGTAGCCGACCTGAGAGGGTGACCGGCCACATTGGGACTGAGACACGGCCCAAACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGGGAAACCCTGATGCAGCGACGCCGCGTGAGCGAAGAAGTATTTCGGTATGTAAAGCTCTATCAGCAGGGAAGAAGAATGACGGTACCTGACTAAGAAGCACCGGCTAAATACGTGCCAGCAGCCGCGGTAATACGTATGGTGCAAGCGTTATCCGGATTTACTGGGTGTAAAGGGAGCGCAGGCGGTACGGCAAGTCTGATGTGAAAGTCCGGGGCTCAACCCCGGTACTGCATTGGAAACTGTCGGACTAGAGTGTCGGAGGGGTAAGTGGAATTCCTAGTGTAGCGGTGAAATGCGTAGATATTAGGAGGAACACCAGTGGCGAAGGCGGCTTACTGGACGATCACTGACGCTGAGGCTCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGAATACTAGGTGTCGGGAGGCATTGCCTTTCGGTGCCGCCGCAAACGCATTAAGTATTCCACCTGGGGAGTACGTTCGCAAGAATGAAACTCAAAGGAATTGACGGGGACCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGAAGCAACGCGAAGAACCTTACCAAGTCTTGACATCCCGGTGACAGAGTATGTAATGTGCTTTCCTTTCGGGGCACCGGAGACAGGTGGTGCATGGTTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCCTGTCCTTAGTAGCCAGCAGTAAGATGGGCACTCTAGGGAGACTGCCAGGGATAACCTGGAGGAAGGCGGGGATGACGTCAAATCATCATGCCCCTTATGACTTGGGCTACACACGTGCTACAATGGCGTAAACAAAGGGAAGCGAGCCTGTGAGGGGGAGCAAATCCCAAAAATAACGTCTCAGTTCGGACTGTAGTCTGCAACCCGACTACACGAAGCTGGAATCGCTAGTAATCGCGAATCAGAATGTCGCGGTGAATACGTTCCCGGGTCTTGTACACACCGCCCGTCACACCATGGGAGTTGGAAATGCCCGAAGTCAGTGACCCAACCGCAAGGAGGGAGCTGCCGAAGGCAGGTTCGATAACTGGG
>923
CCGGACCCGACCGCTATCGGGGTGGGGCTAAGCCATGGGAGTCGCACGCTCCGCCGCTGCGGGGCGTGGCGCACGGCTGAGTAGCACGTGGCTAACCTGCCCTCGGGAGGGGGATAACACCGGGAAACTGGTGCTAATCCCCCATAGGGGAAGGCGCCTGGAAGGGTCCTTCCTCGAAAAGGCCCGGCAGGGGTTAGCGCTGCCGAGCCGCCCGAGGATGGGGCTACGGCCCATCAGGTAGTTGGCGGGGTAACGGCCCGCCAAGCCGATAACGGGTGGGGGCCGTGAGAGCGGGAGCCCCCAGATGGGCACTGAGACAAGGGCCCAGGCCCTAAGGGGCGCACCAGGCGCGAAACCTCCGCAATGCNGGAAACCGTGACGGGGCCACCCCGAGTGCCCCCTTTCCGGGGGCTTTTCCCCGCTGTAGGAAGGCGGGGGAATAAGCGGGGGGCAAGTCTGGTGTCAGCCGCCGCCGTAATACCAGCCCCGCGAGTGGTCGGGACGGTTATTGGGCCTAAAGCGCCCGTAGCCGGCCCGGCAAGTCCCCTCCTAAATCCCCGGGCTCAACCTGGGGACTGGGGGGGATACTGCCGGGCTAGGGGGCGGGAGAGGCCGAGGGTACTCCCGGGGTAGGGGCGAAATCCTATAATCCCGGGAGGACCACCAGTGGCGAAGGCGCTCGGCTGGAACGCGCCCGACGGTGAGGGGCGAAAGCCGGGGGAGCAAACCGGATTAGATACCGGGTAGTCCCGGCTGTAAACGATGCGGGCTAGCTGTTGGGTGGGCTTAGAGCCCACCCAGTGGCGCAGGGAAGCCGTTAAGCCCGCCGCCTGGGGAGTACGGCCGCAAGGCTGAAACTTAAAGGAATTGGCGGGGGAGCACCACAAGGGGTGGAGCCTGCGGTTCAATTGGAGTCAACGCCGGGAATCTCACCGGGGGCGACAGCAGGATGACGGCCAGGCTAACGACCTTGCCTGACGCGCTGAGAGGAGGTGCATGGCCGTCGCCAGCTCGTGCCGTGAGGTGTCCGGTTAAGTCCGGAAACGAGCGAGACCCCTGNCCCCAGTTGCGANNNNNNNCTACGGCCCTGGGGCACACTGGGGGGACTGCCGCCGTTCAAGGCGGAGGAAGGAGGGGGCCACGGCAGGTCAGCATGCCCCGAATCCCCCGGGCTACACGCGGGCTACAATGGCGGGGACAGCGGGTTCCGACCCCGAAAGGGGGAGGCAATCCCTCAAACCCCGCCGCAGTTGGGATCGAGGGCTGCAACTCGCCCTCGTGAACGCGGAATCCCTAGTAACCGCGCGTCAACATCGCGCGGTGAATACGTCCCTGCTCCTTGCACACACCGCCCGTCGCTCCACCCGAGGGGAGAGGGAGTGAGGCCTGGCCGGCTTGGTCGGGTCGAACTCCCTCTCCCTGAGGGGGGAGA
"""

mapping = """
#SampleID	BarcodeSequence	LinkerPrimerSequence	Environment	Description
S1	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env1	S1_Env1
S2	TTCCAGGCAGAT	GGACTACHVGGGTWTCTAAT	Env2	S2_Env2
"""

blast_results = """
# BLASTN 2.2.22 [Sep-27-2009]
# Query: New.CleanUp.ReferenceOTU999
# Database: small_nt
# Fields: Query id, Subject id, % identity, alignment length, mismatches, gap openings, q. start, q. end, s. start, s. end, e-value, bit score
New.CleanUp.ReferenceOTU999	gi|7|emb|X51700.1|	100.00	11	0	0	92	102	367	357	0.25	22.3
# BLASTN 2.2.22 [Sep-27-2009]
# Query: New.CleanUp.ReferenceOTU972
# Database: small_nt
# Fields: Query id, Subject id, % identity, alignment length, mismatches, gap openings, q. start, q. end, s. start, s. end, e-value, bit score
New.CleanUp.ReferenceOTU972	gi|7|emb|T51700.1|	100.00	11	0	0	92	102	367	357	0.25	22.3
# BLASTN 2.2.22 [Sep-27-2009]
# Query: New.CleanUp.ReferenceOTU969
# Database: small_nt
# Fields: Query id, Subject id, % identity, alignment length, mismatches, gap openings, q. start, q. end, s. start, s. end, e-value, bit score
New.CleanUp.ReferenceOTU969	gi|16|emb|Z52700.1|	90.00	13	0	0	33	45	1604	1616	0.016	26.3
"""

exp_txt = """OTU ID	Sequence	Taxonomy	NCBI nr closest match
New.CleanUp.ReferenceOTU972	ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGGGTGCGTAGGCGGATGTTTAAGTGGGATGTGAAATCCCCGGGCTTAACCTGGGGGCTGC	foo;bar;baz	http://foo.com
New.CleanUp.ReferenceOTU969	ATACGTAGGTCCCGAGCGTTGTCCGGATTTACTGGGTGTAAAGGGAGCGTAGACGGCATGGCAAGTCTGAAGTGAAAACCCAGGGCTCAACCCTGGGACTGC	foo;bar;baz	http://foo.com
New.CleanUp.ReferenceOTU964	ATACGGAGGATGCGAGCGTTATCCGGATTTATTGGGTTTAAAGGGTGCGTAGACGGCGAAGCAAGTCTGAAGTGAAAGCCCGGGGCTCAACCGCGGGACTGC	foo;bar;baz	http://foo.com
New.CleanUp.ReferenceOTU999	ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGGGTGCGTAGGCGGATGTTTAAGTGGGATGTGAAATCCCCGGGCTTAACCTGGGGGCTGC	foo;bar;bazz	http://foo.com
"""

exp_commands = ([[('Filtering out all GG reference OTUs', 'filter_otus_from_otu_table.py -i /a.biom -o /foo/a_novel.biom -e /gg.fasta')], [('Filtering out all OTUs that do not fall within the specified abundance threshold', 'filter_otus_from_otu_table.py -i /foo/a_novel.biom -o /foo/a_novel_min30_max100.biom -n 30 -x 100')], [('Collapsing OTU table by Env', 'summarize_otu_by_cat.py -c /foo/a_novel_min30_max100.biom -o /foo/a_novel_min30_max100_Env.biom -m Env -i /map.txt')], [('Filtering out all GG reference OTUs', 'filter_otus_from_otu_table.py -i /b.biom -o /foo/b_novel.biom -e /gg.fasta')], [('Filtering out all OTUs that do not fall within the specified abundance threshold', 'filter_otus_from_otu_table.py -i /foo/b_novel.biom -o /foo/b_novel_min30_max100.biom -n 30 -x 100')], [('Collapsing OTU table by Env', 'summarize_otu_by_cat.py -c /foo/b_novel_min30_max100.biom -o /foo/b_novel_min30_max100_Env.biom -m Env -i /map.txt')], [('Filtering out all GG reference OTUs', 'filter_otus_from_otu_table.py -i /c.biom -o /foo/c_novel.biom -e /gg.fasta')], [('Filtering out all OTUs that do not fall within the specified abundance threshold', 'filter_otus_from_otu_table.py -i /foo/c_novel.biom -o /foo/c_novel_min30_max100.biom -n 30 -x 100')], [('Collapsing OTU table by Env', 'summarize_otu_by_cat.py -c /foo/c_novel_min30_max100.biom -o /foo/c_novel_min30_max100_Env.biom -m Env -i /map.txt')], [('Merging collapsed OTU tables', 'merge_otu_tables.py -i /foo/a_novel_min30_max100_Env.biom,/foo/b_novel_min30_max100_Env.biom,/foo/c_novel_min30_max100_Env.biom -o /foo/master_otu_table_novel_min30_max100_Env.biom')], [('Filtering OTU table to include only OTUs that appear in at least 5 sample groups', 'filter_otus_from_otu_table.py -i /foo/master_otu_table_novel_min30_max100_Env.biom -o /foo/master_otu_table_novel_min30_max100_Env_ms5.biom -s 5')], [('Filtering representative set to include only the latest candidate OTUs', 'filter_fasta.py -f /rs.fna -o /foo/rs_candidates.fna -b /foo/master_otu_table_novel_min30_max100_Env_ms5.biom')], [("Running uclust to get list of sequences that don't hit the maximum GG similarity threshold", 'parallel_pick_otus_uclust_ref.py -i /foo/rs_candidates.fna -o /foo/most_wanted_candidates_gg.fasta_0.7 -r /gg.fasta -s 0.7 -O 55')], [('Filtering candidate sequences to only include uclust failures', 'filter_fasta.py -f /foo/rs_candidates.fna -s /foo/most_wanted_candidates_gg.fasta_0.7/rs_candidates_failures.txt -o /foo/rs_candidates_failures.fna')], [('BLASTing filtered candidate sequences against nt database', 'parallel_blast.py -i /foo/rs_candidates_failures.fna -o /foo/blast_output -r /nt -D -e 0.000100 -w 25 -O 55')]], '/foo/blast_output/rs_candidates_failures_blast_out.txt', '/foo/rs_candidates_failures.fna', '/foo/master_otu_table_novel_min30_max100_Env_ms5.biom')

exp_rep_set_lookup = {'New.CleanUp.ReferenceOTU999': 'ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGGGTGCGTAGGCGGATGTTTAAGTGGGATGTGAAATCCCCGGGCTTAACCTGGGGGCTGC', '102506': 'ATACGTATGGTGCAAGCGTTATCCGGATTTACTGGGTGTAAAGGGAGCGCAGGCGGTACGGCAAGTCTGATGTGAAAGTCCGGGGCTCAACCCCGGTACTGCAAACGTAGGGTGCAAGCGTTGTCCGGAATTACTGGGTGTAAAGGGAGCGTAGACGGCTGTGCAAGTCTGAAGTGAAAGGCATGGGCTCAACCTGTGGACTGC', 'New.CleanUp.ReferenceOTU972': 'ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGGGTGCGTAGGCGGATGTTTAAGTGGGATGTGAAATCCCCGGGCTTAACCTGGGGGCTGC', 'New.CleanUp.ReferenceOTU969': 'ATACGTAGGTCCCGAGCGTTGTCCGGATTTACTGGGTGTAAAGGGAGCGTAGACGGCATGGCAAGTCTGAAGTGAAAACCCAGGGCTCAACCCTGGGACTGC', 'New.CleanUp.ReferenceOTU964': 'ATACGGAGGATGCGAGCGTTATCCGGATTTATTGGGTTTAAAGGGTGCGTAGACGGCGAAGCAAGTCTGAAGTGAAAGCCCGGGGCTCAACCGCGGGACTGC', '10115': 'ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTTTGTTAAGTTTGATGTGAAATCCCCGGGCTTAACCTGGGAACTGC', '10113': 'ATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTCTGTTAAGTCAGATGTGAAATCCCCGGGCTCCACCTGGGCACTGC'}


if __name__ == "__main__":
    main()
