from data.temp.quopri import *
import pytest
import io

def test_encode():
    input_data = b"Hello, World!\nThis is a test.\tTabs should be quoted."
    expected_output = b"Hello, World!=\nThis is a test!=Tabs should be quoted!=\n"
    assert encodestring(input_data) == expected_output

def test_encode_quotetabs():
    input_data = b"Hello, World!\nThis is a test.\tTabs should be quoted."
    expected_output = b"Hello, World!=\nThis is a test!=Tabs should be quoted!=\n"
    assert encodestring(input_data, quotetabs=True) == expected_output

def test_encode_header():
    input_data = b"Hello, World!\nThis is a test.\tTabs should be quoted."
    expected_output = b"Hello, World!=\nThis is a test!=Tabs should be quoted!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode():
    input_data = b"Hello, World!=\nThis is a test!=Tabs should be quoted!=\n"
    expected_output = b"Hello, World!\nThis is a test.\tTabs should be quoted."
    assert decodestring(input_data) == expected_output

def test_decode_header():
    input_data = b"Hello, World!=\nThis is a test!=Tabs should be quoted!=\n"
    expected_output = b"Hello, World!\nThis is a test.\tTabs should be quoted."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_empty_string():
    input_data = b""
    expected_output = b""
    assert encodestring(input_data) == expected_output

def test_decode_empty_string():
    input_data = b""
    expected_output = b""
    assert decodestring(input_data) == expected_output

def test_encode_special_characters():
    input_data = b"Special characters: !@#$%^&*()_+"
    expected_output = b"Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+"
    assert encodestring(input_data) == expected_output

def test_decode_special_characters():
    input_data = b"Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+"
    expected_output = b"Special characters: !@#$%^&*()_+"
    assert decodestring(input_data) == expected_output

def test_encode_long_line():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification."
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=\n"
    assert encodestring(input_data) == expected_output

def test_decode_long_line():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=\n"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification."
    assert decodestring(input_data) == expected_output

def test_encode_header_space():
    input_data = b"Hello, World! This is a test."
    expected_output = b"Hello, World!=This is a test!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_space():
    input_data = b"Hello, World!=This is a test!=\n"
    expected_output = b"Hello, World! This is a test."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_tab():
    input_data = b"Hello, World!\tThis is a test."
    expected_output = b"Hello, World!=This is a test!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_tab():
    input_data = b"Hello, World!=This is a test!=\n"
    expected_output = b"Hello, World!\tThis is a test."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_underscore():
    input_data = b"Hello, World! This is a test."
    expected_output = b"Hello, World!=This is a test!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_underscore():
    input_data = b"Hello, World!=This is a test!=\n"
    expected_output = b"Hello, World! This is a test."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_special_characters():
    input_data = b"Hello, World! This is a test. Special characters: !@#$%^&*()_+"
    expected_output = b"Hello, World!=This is a test!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_special_characters():
    input_data = b"Hello, World!=This is a test!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=\n"
    expected_output = b"Hello, World! This is a test. Special characters: !@#$%^&*()_+"
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_long_line():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. This is a test."
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=This is a test!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_long_line():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=This is a test!=\n"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. This is a test."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_special_characters_long_line():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_special_characters_long_line():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=\n"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+"
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_special_characters_long_line_with_tabs():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+\tTabs should be quoted."
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=Tabs should be quoted!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_special_characters_long_line_with_tabs():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=Tabs should be quoted!=\n"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+\tTabs should be quoted."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_special_characters_long_line_with_spaces():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+ This is a test."
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=This is a test!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_special_characters_long_line_with_spaces():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=This is a test!=\n"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+ This is a test."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_special_characters_long_line_with_tabs_and_spaces():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+\tTabs should be quoted. This is a test."
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=Tabs should be quoted!=This is a test!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_special_characters_long_line_with_tabs_and_spaces():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=Tabs should be quoted!=This is a test!=\n"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+\tTabs should be quoted. This is a test."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_special_characters_long_line_with_tabs_and_spaces_and_newlines():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+\tTabs should be quoted. This is a test.\nThis is another line."
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=Tabs should be quoted!=This is a test!=\nThis is another line!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_special_characters_long_line_with_tabs_and_spaces_and_newlines():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=Tabs should be quoted!=This is a test!=\nThis is another line!=\n"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+\tTabs should be quoted. This is a test.\nThis is another line."
    assert decodestring(input_data, header=True) == expected_output

def test_encode_header_special_characters_long_line_with_tabs_and_spaces_and_newlines_and_special_characters():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification. Special characters: !@#$%^&*()_+\tTabs should be quoted. This is a test.\nThis is another line. Special characters: !@#$%^&*()_+"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=Tabs should be quoted!=This is a test!=\nThis is another line!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=\n"
    assert encodestring(input_data, header=True) == expected_output

def test_decode_header_special_characters_long_line_with_tabs_and_spaces_and_newlines_and_special_characters():
    input_data = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=Tabs should be quoted!=This is a test!=\nThis is another line!=Special characters: !=@!=#!=!=%!=^!=&!=*!=()_+!=\n"
    expected_output = b"This is a very long line that should be split into multiple lines according to the RFC 1521 specification.