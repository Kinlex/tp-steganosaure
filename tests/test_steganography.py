

def test_steno() -> None:
    Message = "ABC"
    Image_path = "/workspaces/tp-steganosaure/tests/images/size.png"
    output_path = "/workspaces/tp-steganosaure/tests/images/decrypt_size.png"
    encrypt(Message, Image_path, output_path)
    assert decrypt(output_path) == "ABC"