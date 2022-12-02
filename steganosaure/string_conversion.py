import numpy


def encode_string(string: str) -> numpy.ndarray:
    bytes_string = string.encode(encoding='utf-8')
    bytes_array = numpy.fromiter(bytes_string, dtype='uint8')
    return numpy.unpackbits(bytes_array)


def decode_bits(bits: numpy.ndarray) -> str:
    bytes_array = numpy.packbits(bits)
    bytes_string = numpy.ndarray.tobytes(bytes_array)
    return bytes_string.decode(encoding='utf-8')
