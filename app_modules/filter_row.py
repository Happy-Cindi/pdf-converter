def FilterRow(row):
    filteref_row = [
        str(cell) for cell in row if cell is not None and str(cell).strip() != ""
    ]

    return filteref_row
