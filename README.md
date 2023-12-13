GitHub rejects files larger than 100MiB, so I split the file into three using `split`. Reconstruct the file like this:
```
cat foo2.parquet_* > foo2.parquet
```

Then run this query:
```
python3 query.py
```
