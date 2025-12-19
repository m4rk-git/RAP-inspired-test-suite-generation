from data.temp.quopri import *
import pytest
import io

def test_encode():
    input_data = b"Hello, world!\nThis is a test."
    expected_output = b"Hello, world!=\nThis is a test!=\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False)
    assert output.getvalue() == expected_output

def test_encode_quotetabs():
    input_data = b"Hello, world!\nThis is a test.\tWith tabs."
    expected_output = b"Hello, world!=\nThis is a test!=\tWith tabs!=\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_header():
    input_data = b"Hello, world!\nThis is a test. With spaces."
    expected_output = b"Hello, world!=\nThis is a test!= With spaces!=\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False, True)
    assert output.getvalue() == expected_output

def test_decode():
    input_data = b"Hello, world!=\nThis is a test!=\n"
    expected_output = b"Hello, world!\nThis is a test.\n"
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output)
    assert output.getvalue() == expected_output

def test_decode_header():
    input_data = b"Hello, world!=\nThis is a test!= With spaces!=\n"
    expected_output = b"Hello, world!\nThis is a test. With spaces.\n"
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_long_line():
    input_data = b"Hello, world! This is a very long line that should be split into multiple lines."
    expected_output = b"Hello, world! This is a very long line that should be split into multiple lines!=\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False)
    assert output.getvalue() == expected_output

def test_encode_long_line_quotetabs():
    input_data = b"Hello, world! This is a very long line that should be split into multiple lines.\tWith tabs."
    expected_output = b"Hello, world! This is a very long line that should be split into multiple lines!=\tWith tabs!=\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_long_line_header():
    input_data = b"Hello, world! This is a very long line that should be split into multiple lines. With spaces."
    expected_output = b"Hello, world! This is a very long line that should be split into multiple lines!= With spaces!=\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False, True)
    assert output.getvalue() == expected_output

def test_decode_long_line():
    input_data = b"Hello, world! This is a very long line that should be split into multiple lines!=\n"
    expected_output = b"Hello, world! This is a very long line that should be split into multiple lines.\n"
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output)
    assert output.getvalue() == expected_output

def test_decode_long_line_header():
    input_data = b"Hello, world! This is a very long line that should be split into multiple lines!= With spaces!=\n"
    expected_output = b"Hello, world! This is a very long line that should be split into multiple lines. With spaces.\n"
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_empty_string():
    input_data = b""
    expected_output = b""
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False)
    assert output.getvalue() == expected_output

def test_encode_empty_string_quotetabs():
    input_data = b""
    expected_output = b""
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_empty_string_header():
    input_data = b""
    expected_output = b""
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False, True)
    assert output.getvalue() == expected_output

def test_decode_empty_string():
    input_data = b""
    expected_output = b""
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output)
    assert output.getvalue() == expected_output

def test_decode_empty_string_header():
    input_data = b""
    expected_output = b""
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_special_characters():
    input_data = b"Hello, world! This is a test with special characters: !@#$%^&*()_+{}|:\"<>?"
    expected_output = b"Hello, world!= This is a test with special characters: !=@#$%^&*()_+{}|:\"<>?\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False)
    assert output.getvalue() == expected_output

def test_encode_special_characters_quotetabs():
    input_data = b"Hello, world! This is a test with special characters: !@#$%^&*()_+{}|:\"<>?"
    expected_output = b"Hello, world!= This is a test with special characters: !=@#$%^&*()_+{}|:\"<>?\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_special_characters_header():
    input_data = b"Hello, world! This is a test with special characters: !@#$%^&*()_+{}|:\"<>?"
    expected_output = b"Hello, world!= This is a test with special characters: !=@#$%^&*()_+{}|:\"<>?\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False, True)
    assert output.getvalue() == expected_output

def test_decode_special_characters():
    input_data = b"Hello, world!= This is a test with special characters: !=@#$%^&*()_+{}|:\"<>?\n"
    expected_output = b"Hello, world! This is a test with special characters: !@#$%^&*()_+{}|:\"<>?\n"
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output)
    assert output.getvalue() == expected_output

def test_decode_special_characters_header():
    input_data = b"Hello, world!= This is a test with special characters: !=@#$%^&*()_+{}|:\"<>?\n"
    expected_output = b"Hello, world! This is a test with special characters: !@#$%^&*()_+{}|:\"<>?\n"
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_binary_data():
    input_data = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    expected_output = b"=00=01=02=03=04=05=06=07=08=09=0A=0B=0C=0D=0E=0F\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False)
    assert output.getvalue() == expected_output

def test_encode_binary_data_quotetabs():
    input_data = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    expected_output = b"=00=01=02=03=04=05=06=07=08=09=0A=0B=0C=0D=0E=0F\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_binary_data_header():
    input_data = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    expected_output = b"=00=01=02=03=04=05=06=07=08=09=0A=0B=0C=0D=0E=0F\n"
    output = io.BytesIO()
    encode(io.BytesIO(input_data), output, False, True)
    assert output.getvalue() == expected_output

def test_decode_binary_data():
    input_data = b"=00=01=02=03=04=05=06=07=08=09=0A=0B=0C=0D=0E=0F\n"
    expected_output = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output)
    assert output.getvalue() == expected_output

def test_decode_binary_data_header():
    input_data = b"=00=01=02=03=04=05=06=07=08=09=0A=0B=0C=0D=0E=0F\n"
    expected_output = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    output = io.BytesIO()
    decode(io.BytesIO(input_data), output, True)
    assert output.getvalue() == expected_output

def test_encode_decode_cycle():
    input_data = b"Hello, world! This is a test with special characters: !@#$%^&*()_+{}|:\"<>? And binary data: \x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    encoded_data = encodestring(input_data)
    decoded_data = decodestring(encoded_data)
    assert decoded_data == input_data

def test_encode_decode_cycle_quotetabs():
    input_data = b"Hello, world! This is a test with special characters: !@#$%^&*()_+{}|:\"<>? And binary data: \x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    encoded_data = encodestring(input_data, quotetabs=True)
    decoded_data = decodestring(encoded_data)
    assert decoded_data == input_data

def test_encode_decode_cycle_header():
    input_data = b"Hello, world! This is a test with special characters: !@#$%^&*()_+{}|:\"<>? And binary data: \x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    encoded_data = encodestring(input_data, header=True)
    decoded_data = decodestring(encoded_data)
    assert decoded_data == input_data

def test_encode_decode_cycle_long_line():
    input_data = b"Hello, world! This is a very long line that should be split into multiple lines. And binary data: \x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    encoded_data = encodestring(input_data)
    decoded_data = decodestring(encoded_data)
    assert decoded_data == input_data

def test_encode_decode_cycle_long_line_quotetabs():
    input_data = b"Hello, world! This is a very long line that should be split into multiple lines. And binary data: \x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    encoded_data = encodestring(input_data, quotetabs=True)
    decoded_data = decodestring(encoded_data)
    assert decoded_data == input_data

def test_encode_decode_cycle_long_line_header():
    input_data = b"Hello, world! This is a very long line that should be split into multiple lines. And binary data: \x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
    encoded_data = encodestring(input_data, header=True)
    decoded_data = decodestring(encoded_data)
    assert decoded_data == input_data

def test_encode_decode_cycle_empty_string():
    input_data = b""
    encoded_data = encodestring(input_data)
    decoded_data = decodestring(encoded_data)
    assert decoded