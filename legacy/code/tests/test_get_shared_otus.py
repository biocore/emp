#!/usr/bin/env python
#file test_get_shared_otus.py

__author__ = "Luke Ursell"
__copyright__ = "Copyright 2011, The QIIME Project" #consider project name
__credits__ = ["Luke Ursell, Yoshiki Baeza"] #remember to add yourself
__license__ = "GPL"
__version__ = "1.5.0-dev"
__maintainer__ = "Luke Ursell"
__email__ = "lkursell@gmail.com"
__status__ = "Development"

from cogent.util.unit_test import TestCase, main
from biom.parse import parse_biom_table

from emp.get_shared_otus import get_shared_otus

class TopLevelTest(TestCase):

    def setUp(self):
        # Looking for OTU0 and OTU1 that are present with min count 1 in 100 percent of samples
        self.get_shared_otus_1_1_input = """{"rows": [{"id": "0", "metadata": null}, {"id": "1", "metadata": null}, {"id": "2", "metadata": null}, {"id": "3", "metadata": null}, {"id": "4", "metadata": null}], "format": "Biological Observation Matrix 0.9.1-dev", "data": [[0, 0, 1.0], [0, 1, 1.0], [0, 2, 1.0], [1, 0, 2.0], [1, 1, 2.0], [1, 2, 2.0], [3, 0, 2.0], [3, 2, 2.0], [4, 1, 5.0]], "columns": [{"id": "Sample1", "metadata": null}, {"id": "Sample2", "metadata": null}, {"id": "Sample3", "metadata": null}], "generated_by": "BIOM-Format 0.9.1-dev", "matrix_type": "sparse", "shape": [5, 3], "format_url": "http://biom-format.org", "date": "2012-08-15T12:52:58.782757", "type": "OTU table", "id": null, "matrix_element_type": "float"}"""
        self.get_shared_otus_1_1_result = ['OTU_ID\tMin_count\tPercentage\n', '1\t1\t1.0\n', '0\t1\t1.0\n']
        
        #Looking for OTU1 and OTU3 present with min count 2 in at least 60% samples
        self.get_shared_otus_2_06_input = """{"rows": [{"id": "0", "metadata": null}, {"id": "1", "metadata": null}, {"id": "2", "metadata": null}, {"id": "3", "metadata": null}, {"id": "4", "metadata": null}], "format": "Biological Observation Matrix 0.9.1-dev", "data": [[0, 0, 1.0], [0, 1, 1.0], [0, 2, 1.0], [1, 0, 2.0], [1, 1, 2.0], [1, 2, 2.0], [3, 0, 2.0], [3, 2, 2.0], [4, 1, 5.0]], "columns": [{"id": "Sample1", "metadata": null}, {"id": "Sample2", "metadata": null}, {"id": "Sample3", "metadata": null}], "generated_by": "BIOM-Format 0.9.1-dev", "matrix_type": "sparse", "shape": [5, 3], "format_url": "http://biom-format.org", "date": "2012-08-15T12:52:58.782757", "type": "OTU table", "id": null, "matrix_element_type": "float"}"""
        self.get_shared_otus_2_06_result = ['OTU_ID\tMin_count\tPercentage\n', '1\t2\t1.0\n', '3\t2\t0.666666666667\n']

        # No taxa are shared when looking for min count 5 in 90% samples
        self.get_shared_otus_5_09_input = """{"rows": [{"id": "0", "metadata": null}, {"id": "1", "metadata": null}, {"id": "2", "metadata": null}, {"id": "3", "metadata": null}, {"id": "4", "metadata": null}], "format": "Biological Observation Matrix 0.9.1-dev", "data": [[0, 0, 1.0], [0, 1, 1.0], [0, 2, 1.0], [1, 0, 2.0], [1, 1, 2.0], [1, 2, 2.0], [3, 0, 2.0], [3, 2, 2.0], [4, 1, 5.0]], "columns": [{"id": "Sample1", "metadata": null}, {"id": "Sample2", "metadata": null}, {"id": "Sample3", "metadata": null}], "generated_by": "BIOM-Format 0.9.1-dev", "matrix_type": "sparse", "shape": [5, 3], "format_url": "http://biom-format.org", "date": "2012-08-15T12:52:58.782757", "type": "OTU table", "id": null, "matrix_element_type": "float"}"""
        self.get_shared_otus_5_09_result = ['No taxa are shared']

    def test_get_shared_otus(self):
        otu_table = parse_biom_table(self.get_shared_otus_1_1_input)
        exp = get_shared_otus([otu_table],1,1)
        self.assertEqual(self.get_shared_otus_1_1_result,exp)

        otu_table_2 = parse_biom_table(self.get_shared_otus_2_06_input)
        exp_2_06 = get_shared_otus([otu_table_2],2,0.6)
        self.assertEqual(self.get_shared_otus_2_06_result,exp_2_06)

        otu_table_3 = parse_biom_table(self.get_shared_otus_5_09_input)
        exp_5_09 = get_shared_otus([otu_table_3],5,0.9)
        self.assertEqual(self.get_shared_otus_5_09_result,exp_5_09)


if __name__ == "__main__":
    main()
