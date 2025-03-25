from app.io.input import input_from_file, input_from_file_using_pandas


def test_input_from_file1():
    test_file = "../../test_data/test_input_from_file1.txt"
    expected = "Testing input_from_file 1"

    actual = input_from_file(test_file)

    assert expected == actual

def test_input_from_file2():
    test_file = "../../test_data/test_input_from_file2.txt"
    expected = "Testing input_from_file two"

    actual = input_from_file(test_file)

    assert expected == actual

def test_input_from_file3():
    test_file = "../../test_data/test_input_from_file3.txt"
    expected = "Testing input_from_file |||"

    actual = input_from_file(test_file)

    assert expected == actual