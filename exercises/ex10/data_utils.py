"""Dictionary related utility functions."""

__author__ = "730668363"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # Loop through each element (dictionary) of the list
    for elem in table:
        # For each dictionary {elem}, get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # Loop through keys of one row of table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # For each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(table_data: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns a new column-based table with only the first N rows of data for each column."""
    new_table_data: dict[str, list[str]] = {}
    for keys in table_data:
        first_n_values: list[str] = []
        idx: int = 0
        while idx < rows and idx < len(table_data[keys]):
            first_n_values.append(table_data[keys][idx])
            idx += 1
        new_table_data[keys] = first_n_values
    return new_table_data


def select(table_data: dict[str, list[str]], copy_columns: list[str]) -> dict[str, list[str]]:
    """Returns a new column-based table taht contains only a specific subset of the original columns."""
    new_data_table: dict[str, list[str]] = {}
    for keys in copy_columns:
        new_data_table[keys] = table_data[keys]
    return new_data_table


def concat(table_data1: dict[str, list[str]], table_data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a new column-based table with two column-based tables combined."""
    new_table: dict[str, list[str]] = {}
    for keys in table_data1:
        new_table[keys] = table_data1[keys]
    for keys in table_data2:
        if keys in new_table:
            new_table[keys] += table_data2[keys]
        else:
            new_table[keys] = table_data2[keys]
    return new_table