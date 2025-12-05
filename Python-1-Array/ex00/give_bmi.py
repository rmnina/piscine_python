import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    try:
        assert isinstance(height, list) and isinstance(weight, list), \
            "Wrong datatype used"
        assert len(height) == len(weight), "Lists are not the same size"
        assert [x for x in height if isinstance(x, int) or
                isinstance(x, float)], "Wrong datatype in height"
        assert [x for x in weight if isinstance(x, int) or
                isinstance(x, float)], "Wrong datatype in weight"
    except AssertionError as error:
        print(f"Assertion Error: {error}")
        exit(1)

    np_height = np.array(height)
    np_weight = np.array(weight)

    bmi = np_weight / np.square(np_height)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        assert isinstance(bmi, list) and isinstance(limit, int), \
            "Wrong datatype used"
        assert [x for x in bmi if isinstance(x, int) or
                isinstance(x, float)], "Wrong datatype in bmi"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        exit(1)

    np_bmi = np.array(bmi)

    ret = np_bmi > limit

    return ret.tolist()
