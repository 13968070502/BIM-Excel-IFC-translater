def read_in_col(coords, ws):
    """Read data from column starting below given coordinates."""
    data = []
    for row in range(coords[0], ws.max_row+1):
        data.append(ws.cell(row=row, column=coords[1]).value)
    return data


def read_in_row(coords, ws):
    """Read data from row starting right of given coordinates."""
    data = []
    for col in range(coords[1], ws.max_column+1):
        data.append(ws.cell(row=coords[0], column=col).value)
    return data
