import os 
import numpy
from steganosaure.image_io import load_image, save_image
#  Sauvegarde  -> Chargé l'image -> compare originale et sauvegarde


def test_crucial() -> None:
    image_path = "/workspaces/tp-steganosaure/tests/images/size.png"
    image_originale = load_image(image_path)
    save_image(image_originale, image_path)
    image_recharge = load_image(image_path)
    numpy.testing.assert_array_equal(image_originale, image_recharge)
