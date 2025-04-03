import dask.dataframe as dd
import numpy as np
import pandas as pd


def assert_output_is_equals_to(actual_output, expected_output):
    def wrapper(actual_output):
        if isinstance(actual_output, pd.DataFrame):
            pd.testing.assert_frame_equal(
                actual_output.reset_index(drop=True).sort_index(axis=1),
                expected_output.reset_index(drop=True).sort_index(axis=1),
            )
        elif isinstance(actual_output, dd.DataFrame):
            pd.testing.assert_frame_equal(
                actual_output.compute().reset_index(drop=True).sort_index(axis=1),
                expected_output.reset_index(drop=True).sort_index(axis=1),
            )
        else:
            raise Exception("Wrong output class")

    return wrapper(actual_output)


def load_from_json(json_path, dtype_dict=None):
    expected = pd.read_dataframe(json_path, orient="table").replace([np.nan], [None])
    if dtype_dict is not None:
        expected = expected.astype(dtype=dtype_dict)
    return expected
