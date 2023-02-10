import sys
sys.path.append('app')


import os
import pytest
from utils.file_reader import read_map_from_file

def test_read_map_from_file_returns_map_for_valid_input():
    # Create a sample input file
    with open("sample.txt", "w") as f:
        f.write("111\n")
        f.write("101\n")

    map = read_map_from_file("sample.txt")
    assert len(map) == 2
    assert len(map[0]) == 3
    assert map[0] == [1, 1, 1]
    assert map[1] == [1, 0, 1]
    
    # Clean up the sample input file
    os.remove("sample.txt")

def test_read_map_from_file_returns_map_for_invalid_input():
    # Create a sample input file
    with open("sample.txt", "w") as f:
        f.write("1 1 1\n")
        f.write("a 3 1\n")

    with pytest.raises(Exception) as excinfo:
        map = read_map_from_file("sample.txt")
    assert "Invalid character found" in str(excinfo.value)
    # Clean up the sample input file
    os.remove("sample.txt")

def test_read_map_from_file_raises_exception_for_file_not_found():
    with pytest.raises(Exception) as excinfo:
        map = read_map_from_file("nonexistent.txt")
    assert "File not found" in str(excinfo.value)
    
def test_read_map_from_file_raises_exception_for_empty_file():
    # Create an empty input file
    with open("empty.txt", "w") as f:
        pass

    with pytest.raises(Exception) as excinfo:
        map = read_map_from_file("empty.txt")
    assert "File is empty" in str(excinfo.value)
    
    # Clean up the empty input file
    os.remove("empty.txt")