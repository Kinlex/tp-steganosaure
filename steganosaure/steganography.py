import pathlib
import numpy
from bits_manipulation import retrieve_least_significant_bits, modify_least_significant_bits, pad_message
from image_io import load_image, save_image
from string_conversion import encode_string, decode_bits

def encrypt(message: str, input_image_path: pathlib.Path, output_image_path: pathlib.Path) -> None:
    Encoded_message = encode_string(message)
    
    