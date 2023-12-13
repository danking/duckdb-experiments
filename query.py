import duckdb
duckdb.sql('''
copy (
  select
    "#CHROM",
    "POS",
    "ID",
    "REF",
    "ALT",
    "QUAL",
    "FILTER",
    "INFO",
    "FORMAT",
    unnest(range(len(string_split(entries, '	')))) as col_idx,
    string_split(entries, '	')[col_idx + 1] as entry
  from 'foo2.parquet'
) to 'foo3.parquet'
'''
)
