# Quick test between Pandas, Polars and PySpark

This is a quick test comparing how the libraries Pandas, Polars, and PySpark handle very large files.

The test was executed on a Macbook M1 with 8Gb of memory.

These are the results:

| Data Size | Pandas  | Polars | PySpark |
|-----------|---------|--------|---------|
| 1GB       | 19.36s  | 6.77s  | 10.34s  |
| 2GB       | 68.02s  | 19.57s | 19.41s  |
| 5GB       | 370.42s | 140.12s| 41.45s  |
| 12GB      | Crash   | Crash  | 86.18s  |
