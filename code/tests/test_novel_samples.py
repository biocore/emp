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

"""Test suite for the novel_samples.py module."""

from cogent.util.unit_test import TestCase, main

from emp_isme14.novel_samples import compute_sample_novelty

class NovelSamplesTests(TestCase):
    def setUp(self):
        """Create some sample data to use in the tests."""
        self.table1_f = table1.split('\n')
        self.table2_f = table2.split('\n')
        self.ref_seqs_f = ref_seqs.split('\n')

    def test_compute_sample_novelty(self):
        """Test computing the novelty of a sample using various metrics."""
        exp = [('B', 4, 57.692307692307686), ('C', 3, 57.142857142857139),
               ('A', 0, 0.0)]
        obs = compute_sample_novelty([self.table1_f, self.table2_f],
                                     self.ref_seqs_f)
        self.assertFloatEqual(obs, exp)

        # Test that table order doesn't matter.
        obs = compute_sample_novelty([self.table2_f, self.table1_f],
                                     self.ref_seqs_f)
        self.assertFloatEqual(obs, exp)

        # Test duplicate table (should still work).
        exp = [('B', 2, 44.444444444444443), ('A', 0, 0.0)]
        obs = compute_sample_novelty([self.table1_f, self.table1_f],
                                     self.ref_seqs_f)
        self.assertFloatEqual(obs, exp)


# #OTU ID	A	B
# GG1	1.0	5.0
# New2	0.0	1.0
# GG2	10.0	0.0
# New1	0.0	3.0
table1 = """
{"rows": [{"id": "GG1", "metadata": null}, {"id": "New2", "metadata": null}, {"id": "GG2", "metadata": null}, {"id": "New1", "metadata": null}], "format": "Biological Observation Matrix 1.0.0", "data": [[0, 0, 1.0], [0, 1, 5.0], [1, 1, 1.0], [2, 0, 10.0], [3, 1, 3.0]], "columns": [{"id": "A", "metadata": null}, {"id": "B", "metadata": null}], "generated_by": "BIOM-Format 1.0.0c", "matrix_type": "sparse", "shape": [4, 2], "format_url": "http://biom-format.org", "date": "2012-08-10T10:36:36.386189", "type": "OTU table", "id": null, "matrix_element_type": "float"}
"""

# #OTU ID	B	C
# GG3	4.0	3.0
# GG1	2.0	0.0
# New1	7.0	1.0
# New3	3.0	2.0
# New4	1.0	1.0
table2 = """
{"rows": [{"id": "GG3", "metadata": null}, {"id": "GG1", "metadata": null}, {"id": "New1", "metadata": null}, {"id": "New3", "metadata": null}, {"id": "New4", "metadata": null}], "format": "Biological Observation Matrix 1.0.0", "data": [[0, 0, 4.0], [0, 1, 3.0], [1, 0, 2.0], [2, 0, 7.0], [2, 1, 1.0], [3, 0, 3.0], [3, 1, 2.0], [4, 0, 1.0], [4, 1, 1.0]], "columns": [{"id": "B", "metadata": null}, {"id": "C", "metadata": null}], "generated_by": "BIOM-Format 1.0.0c", "matrix_type": "sparse", "shape": [5, 2], "format_url": "http://biom-format.org", "date": "2012-08-10T10:38:44.625396", "type": "OTU table", "id": null, "matrix_element_type": "float"}
"""

ref_seqs = """
>GG1
ACGCTGGCGGCAGG
>GG2
TTGATCCTGGCTCA
>GG4
AGAGTTTGATCCTG
>GG3
CCGGACCCGACCGC
"""


if __name__ == "__main__":
    main()
