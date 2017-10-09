#!/usr/bin/env python
import click

import pandas as pd
import numpy as np

from os import mkdir
from os.path import basename, join
from functools import partial


DATA_TYPES_NUMERIC = ('int', 'float')

FINAL_LIST = [
    'study_id', 'host_scientific_name',
    'latitude_deg', 'longitude_deg',
    'envo_biome_3', 'empo_3', 
    'temperature_deg_c', 'ph', 'salinity_psu',
    'oxygen_mg_per_l', 'nitrate_umol_per_l']

COLS_TO_IGNORE = [
    # Sample - not relevant or too many values
    '#SampleID', 'BarcodeSequence', 'LinkerPrimerSequence', 'Description',
    'host_subject_id', 'depth_m', 'elevation_m', 'altitude_m', 'country', 
    'collection_timestamp', 'sample_taxid', 
    # Study - not relevant or redundant with study_id
    'title', 'principal_investigator', 'doi', 'ebi_accession',
    # Prep
    'target_gene', 'target_subfragment', 'pcr_primers', 'illumina_technology',
    'extraction_center', 'run_center', 'run_date',
    # Sequences
    'read_length_bp', 'sequences_split_libraries',
    'observations_closed_ref_greengenes', 'observations_closed_ref_silva',
    'observations_open_ref_greengenes', 'observations_deblur_90bp',
    'observations_deblur_100bp', 'observations_deblur_150bp',
    # Subsets
    'all_emp', 'qc_filtered', 'subset_10k', 'subset_5k', 'subset_2k',
    # Sample type - redundant with empo_3 and envo_biome_3
    'sample_scientific_name', 'envo_biome_0', 'envo_biome_1', 'envo_biome_2',
    'envo_biome_4', 'envo_biome_5', 'empo_0', 'empo_1', 'empo_2', 'env_feature',
    'env_material', 'env_biome', 
    # Alpha-diversity
    'adiv_observed_otus', 'adiv_chao1', 'adiv_shannon', 'adiv_faith_pd',
    # Nutrients - redundant with nitrate_umol_per_l
    'phosphate_umol_per_l', 'ammonium_umol_per_l', 'sulfate_umol_per_l',
    # Taxonomy - redundant with host_scientific_name
    'host_superkingdom', 'host_kingdom', 'host_phylum', 'host_class',
    'host_order', 'host_family', 'host_genus', 'host_species', 
    'host_common_name', 'host_taxid',
    # Duplicated
    'host_common_name_provided']

DATA_FIELDS = {
    # Study
    'study_id': 'categorical',
    #  Taxonomy
    'sample_taxid': 'categorical', 'sample_scientific_name': 'categorical',
    'host_taxid': 'categorical', 'host_common_name': 'categorical',
    'host_scientific_name': 'categorical', 'host_superkingdom': 'categorical',
    'host_kingdom': 'categorical', 'host_phylum': 'categorical',
    'host_class': 'categorical', 'host_order': 'categorical',
    'host_family': 'categorical', 'host_genus': 'categorical',
    'host_species': 'categorical',
    # Geography
    'collection_timestamp': 'categorical', 'country': 'categorical',
    'latitude_deg': 'float', 'longitude_deg': 'float', 'altitude_m': 'float',
    'depth_m': 'float', 'elevation_m': 'float',
    # Ontology
    'env_biome': 'categorical', 'env_feature': 'categorical',
    'env_material': 'categorical', 'envo_biome_0': 'categorical',
    'envo_biome_1': 'categorical', 'envo_biome_2': 'categorical',
    'envo_biome_3': 'categorical', 'envo_biome_4': 'categorical',
    'envo_biome_5': 'categorical', 'empo_0': 'categorical',
    'empo_1': 'categorical', 'empo_2': 'categorical', 'empo_3': 'categorical',
    # Environment
    'temperature_deg_c': 'float', 'ph': 'float', 'salinity_psu': 'float',
    'oxygen_mg_per_l': 'float', 'phosphate_umol_per_l': 'float',
    'ammonium_umol_per_l': 'float', 'nitrate_umol_per_l': 'float',
    'sulfate_umol_per_l': 'float'}


@click.option('--mapping', type=click.File('rb'), help='mapping filepath')
@click.option('--output', type=click.Path(exists=False),
              help='output filepath')
@click.command()
def servicio(mapping, output):
    if mapping is None:
        raise ValueError("You need to pass a mapping")
    if output is None:
        raise ValueError("You need to pass a output")

    mkdir(output)
    pj = partial(join, output)
    mn = basename(mapping.name)
    quartiles_fp = pj(mn + '.quartiles.tsv')
    deciles_fp = pj(mn + '.deciles.tsv')

    map_ = pd.read_csv(mapping, sep='\t', dtype=str)
    map_.set_index('#SampleID', inplace=True)

    # initial cleaning
    # ignore all columns that are part of COLS_TO_IGNORE or alpha div
    for column_name in map_.columns.values:
        if column_name in set(COLS_TO_IGNORE) - set(FINAL_LIST):
            map_[column_name] = np.nan
        else:
            dt = DATA_FIELDS[column_name]

    # remove all columns with only NaN
    map_.dropna(axis=1, how='all', inplace=True)

    # generate our new DataFrames
    quartiles = map_.copy(deep=True)
    deciles = map_.copy(deep=True)
    for column_name in FINAL_LIST:
        dt = DATA_FIELDS[column_name]
        if dt in DATA_TYPES_NUMERIC:
            # we need to calculate the bins so we know that nothing else
            # will fail
            quartiles[column_name] = pd.to_numeric(
                quartiles[column_name], errors='coerce')
            deciles[column_name] = pd.to_numeric(
                deciles[column_name], errors='coerce')
            quartiles[column_name], qbins = pd.qcut(
                quartiles[column_name], 4, labels=False, retbins=True,
                duplicates='drop')
            deciles[column_name], dbins = pd.qcut(
                deciles[column_name], 10, labels=False, retbins=True,
                duplicates='drop')

            # confirm that we have the expected number of bins
            if len(qbins) != 5:
                quartiles[column_name] = np.nan
            if len(dbins) != 11:
                deciles[column_name] = np.nan
    quartiles.dropna(axis=1, how='all', inplace=True)
    deciles.dropna(axis=1, how='all', inplace=True)

    for column_name in quartiles:
        quartiles[column_name] = _clean_column(quartiles[column_name])
    for column_name in deciles:
        deciles[column_name] = _clean_column(deciles[column_name])
    quartiles.dropna(axis=1, how='all', inplace=True)
    deciles.dropna(axis=1, how='all', inplace=True)

    quartiles.fillna('nan', inplace=True)
    deciles.fillna('nan', inplace=True)

    quartiles.to_csv(quartiles_fp, sep='\t')
    deciles.to_csv(deciles_fp, sep='\t')


def _clean_column(column):
    # let's check the size of the groups and discard anything that
    # has less than 50 samples or represents under 0.03 of the size
    counts = pd.DataFrame(
        [column.value_counts(),
         column.value_counts(normalize=True)],
        index=['counts', 'perc']).T
    check = (counts['counts'] < 50) | (counts['perc'] < 0.003)
    replace = check.index[check]
    if replace.size != 0:
        column.replace({v: np.nan for v in replace}, inplace=True)

    if column.nunique() == 1:
        column = np.nan

    return column


if __name__ == '__main__':
    servicio()
