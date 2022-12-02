import numpy
from steganosaure.string_conversion import encode_string, decode_bits


def test_encode() -> None:
    test_array = numpy.array([0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1])
    numpy.testing.assert_array_equal(encode_string("ABC"), test_array)


def test_decode() -> None:
    test_array = numpy.array([0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1])
    assert decode_bits(test_array) == "ABC"