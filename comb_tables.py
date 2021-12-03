#! /usr/bin/env python3
"""
Script to combine multiple tables with different column names.

- Read the data.
- Rename the columns to match the other column names.
- Export the dataframe.

Requirement:
- The data should be in the first sheet of the excel file.
- User need to modify the 'dict' variable to rename the columns.
  The variable can be empty if rename is unnecessary.
- User need to modify the index of dataframe in 'df_list' to be renamed.
  The index starts with '0' and it is according to the position in the arguments.

Usage:
    python3 comb_tables.py -v --files data1.xlsx data2.xlsx -o output.xlsx
"""


import argparse

import pandas as pd


# Create argument parser
parser = argparse.ArgumentParser(description="Combine multiple tables with different column names.")
required_argument = parser.add_argument_group("required named arguments")
parser.add_argument("-v", "--verbose", action="store_true", help="verbosity")
required_argument.add_argument("--files", nargs="+", help="excel filenames", required=True)
required_argument.add_argument("-o", "--output", help="output filename", required=True)

args = parser.parse_args()

# Store arguments in variables.
verbose = args.verbose
files = args.files
outFileName = args.output


# Read excel files.
df_list = []
for file in files:
    df_list.append(pd.read_excel(file))

if verbose:
    print("Original Data")
    for df in df_list:
        print(df)
        print()


# Dictionary of column names and new column names.
# The variable can be empty if rename is unnecessary.
dict = {
    "first": "First Name",
    "last": "Last Name",
}

# Rename the columns if necessary.
# Replace the number '1' to the index of dataframe to be renamed.
df_list[1].rename(columns=dict, inplace=True)


# Concatenate the dataframes.
df_output = pd.concat(df_list).reset_index(drop=True)
if verbose:
    print("Combined Data")
    print(df_output)
    print()


# Export to an excel file.
df_output.to_excel(outFileName, index=False)
