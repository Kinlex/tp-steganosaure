import pathlib
import numpy
import skimage


def load_image(image_path: pathlib.Path) -> numpy.ndarray:
    image_array = skimage.io.imread(image_path)
    return skimage.util.img_as_ubyte(image_array)


def save_image(image: numpy.ndarray, image_path: pathlib.Path) -> None:
    skimage.io.imsave(image_path, image, plugin="pil", check_contrast=False)