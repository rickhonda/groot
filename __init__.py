import pandas as pd
import numpy as np
import seaborn as sns
import csv, math, pathlib, os.path

def link(
    data_matrix = None,
    dataset = None,
    target_vector = None,
):
    from groot.ws import Dataset
    return Dataset(
        data_matrix,
        dataset,
        target_vector,
        )

if __name__ == "__main__":
    import groot.__main__
    __main__.main()

