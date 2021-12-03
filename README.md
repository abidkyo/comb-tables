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


## Example Output
```
Original Data
  First Name   Last Name  Gender  Age                        Email
0  Charlotte      Walker  Female   21      c.walker@randatmail.com
1     Ashton  Richardson    Male   19  a.richardson@randatmail.com
2      Ellia     Spencer  Female   28     e.spencer@randatmail.com
3      Edwin      Gibson    Male   29      e.gibson@randatmail.com
4    Brianna       Adams  Female   26       b.adams@randatmail.com

                       Email  Gender  Age     first      last
0    a.miller@randatmail.com  Female   22    Amanda    Miller
1  m.sullivan@randatmail.com  Female   30  Madaline  Sullivan
2      v.reed@randatmail.com    Male   25    Victor      Reed
3     g.payne@randatmail.com  Female   19    Gianna     Payne
4    m.martin@randatmail.com  Female   20   Miranda    Martin


Combined Data
  First Name   Last Name  Gender  Age                        Email
0  Charlotte      Walker  Female   21      c.walker@randatmail.com
1     Ashton  Richardson    Male   19  a.richardson@randatmail.com
2      Ellia     Spencer  Female   28     e.spencer@randatmail.com
3      Edwin      Gibson    Male   29      e.gibson@randatmail.com
4    Brianna       Adams  Female   26       b.adams@randatmail.com
5     Amanda      Miller  Female   22      a.miller@randatmail.com
6   Madaline    Sullivan  Female   30    m.sullivan@randatmail.com
7     Victor        Reed    Male   25        v.reed@randatmail.com
8     Gianna       Payne  Female   19       g.payne@randatmail.com
9    Miranda      Martin  Female   20      m.martin@randatmail.com

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
