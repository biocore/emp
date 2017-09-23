### UniFrac and principal coordinates commands

```
# in a python3 environment
python snappy_unifrac.py <tree> <biom-table> 16 block 64 <output> <weighted_unifrac | unweighted_unifrac>

# in a qiime 1.9.1 environment
principal_coordinates.py -i <distance_matrix> -o <pcoa>
```

### Underlying code

[snappy_unifrac.py](https://gist.github.com/wasade/60db4059e3b7e42bb648db1d10ef72d6) and [scikit-bio code](https://github.com/biocore/scikit-bio/pull/1352)

