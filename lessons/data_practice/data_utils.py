"""Working with CSV Data."""
from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
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
        result[key] = column_vals(table, key)
    return result