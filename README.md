# comb_cols

## Description
Script to combine multiple tables with different column names.

- Read the data as string.
- Rename the columns to match the other column names.
- Export the dataframe.


## Requirement:
- User need to modify the 'dict' variable to rename the columns.
  The variable can be empty if rename is unnecessary.
- The data should be in the first sheet of the excel file.

### Example 'dict' variable
```python
dict = {
    "first": "First Name",
    "last": "Last Name",
}
```


## Usage
```bash
python3 comb_tables.py -v --files data1.xlsx data2.xlsx -o output.xlsx
```

## Dependencies
[pandas](https://pandas.pydata.org/)
[openpyxl](https://openpyxl.readthedocs.io)
```bash
python3 -m pip install pandas openpyxl
```

## Help Message
```bash
usage: comb_tables.py [-h] [-v] --files FILES [FILES ...] -o OUTPUT

Combine multiple tables with different column names.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbosity

required named arguments:
  --files FILES [FILES ...]
                        excel filenames
  -o OUTPUT, --output OUTPUT
                        output filename
```

### Note
Tested with Python 3.8.10 and Pandas 1.3.4
