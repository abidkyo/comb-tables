# comb_cols

## Description
Script to combine multiple tables with different column names.

- Read the data.
- Rename the columns to match the other column names.
- Export the dataframe.


## Requirement:
- The data should be in the first sheet of the excel file.
- User need to modify the `dict` variable to rename the columns.
  The variable can be empty if rename is unnecessary.
- User need to modify the index of dataframe in `df_list` to be renamed.
  The index starts with `0` and it is according to the position in the arguments.

### Example `dict` variable
```python
dict = {
    "first": "First Name",
    "last": "Last Name",
}
```

### Example modify index of dataframe in `df_list`
Replace `1` with the index that you want.
```python
df_list[1].rename(columns=dict, inplace=True)
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
