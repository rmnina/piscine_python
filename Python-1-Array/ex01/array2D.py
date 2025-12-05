import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(family, list) and isinstance(start, int) and \
            isinstance(end, int), "Wrong datatype"
        assert np.abs(start) < len(family) and np.abs(end) < len(family), \
            "Start or end out of range"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        exit(1)

    np_family = np.array(family)
    print(f"My shape is : {np_family.shape}")

    ret = np_family[start:end]
    print(f"My new shape is : {ret.shape}")

    return ret.tolist()
