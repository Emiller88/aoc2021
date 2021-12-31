import pandas as pd

def read_data(input_file_path: str):
    draw_numbers = pd.read_csv(
        input_file_path,
        nrows=1,
        header=None,
        index_col=False,
    )

    with pd.read_csv(input_file_path, skiprows=2, chunksize=5, header=None) as reader:
        reader
        for chunk in reader:
            print(chunk)

    return draw_numbers
