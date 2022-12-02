import numpy
from steganosaure.bits_manipulation import retrieve_least_significant_bits, modify_least_significant_bits, pad_message

[3, 7 , 16, 2]
[0, 0, 1, 1]
[2, 6, 17, 3]
# 0b00000000 = 0
#     
# 0b000000001 = 1
# 0b000000010 = 2
# 0b000000010 = 2
# 0b000000110 = 6


def test_retrieve_lsb() -> None:
    test_array = numpy.array([1, 2, 3, 7])
    test_bits = numpy.array([1, 0, 1, 1])
    numpy.testing.assert_array_equal(retrieve_least_significant_bits(test_array), test_bits)


def test_modify_lsb() -> None:
    test_message = numpy.array([0, 0, 1, 1])
    test_image = numpy.array([3, 7 , 16, 2])
    result = numpy.array([2, 6, 17, 3])
    numpy.testing.assert_array_equal(modify_least_significant_bits(test_message, test_image), result)


def test_pad() -> None:
    test_message = numpy.array([0, 0, 1])
    test_image = numpy.array([2, 6, 17, 3, 1, 1, 1, 1, 1])
    assert len(test_image) == len(pad_message(test_image, test_message))