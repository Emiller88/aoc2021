import pandas as pd


def read_data(input_file_path: str):
    draw_numbers = pd.read_csv(
        input_file_path,
        nrows=1,
        header=None,
        index_col=False,
    )

    boards = []
    with pd.read_csv(
        input_file_path, skiprows=2, chunksize=5, header=None, sep=r"\s{1,}"
    ) as reader:
        reader
        for chunk in reader:
            boards.append(chunk)

    return draw_numbers, boards
