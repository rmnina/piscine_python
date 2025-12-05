from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.array:

    ERRORS = (FileNotFoundError, IsADirectoryError, PermissionError,
              AttributeError, UnidentifiedImageError)

    try:
        with Image.open(path) as img:
            img_data = np.array(img)
            print(f"The shape of the image is: {img_data.shape}")
            return img_data
    except ERRORS as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        exit(1)
