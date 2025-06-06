# combine-csv-into-xlsx
Combine multiple CSV files into an XLSX workbook or merge multiple XLSX files into a single CSV.

## Usage

```
python combine-files.py [--mode MODE] [--path PATH] [--output OUTPUT]
```

- `--mode csv_to_xlsx` (default) merges all CSV files in `PATH` into an Excel workbook.
- `--mode xlsx_to_csv` merges all XLSX files in `PATH` into one CSV file.
