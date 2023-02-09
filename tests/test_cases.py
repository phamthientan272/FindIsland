import sys
sys.path.append('app')

from utils.file_reader import read_map_from_file
from algo.island_counter import Map

def test_count_island_normal_case_4():
    map = read_map_from_file("tests/map_4.txt")
    m = Map(map)
    n_islands = m.count_islands()
    
    assert n_islands == 4
    
def test_count_island_normal_case_0():
    map = read_map_from_file("tests/map_0.txt")
    m = Map(map)
    n_islands = m.count_islands()
    
    assert n_islands == 0

def test_count_island_normal_case_3():
    map = read_map_from_file("tests/map_3.txt")
    m = Map(map)
    n_islands = m.count_islands()
    
    assert n_islands == 3

def test_count_island_extreme_case_900():
    map = read_map_from_file("tests/map_extreme_900.txt")
    m = Map(map)
    n_islands = m.count_islands()
    
    assert n_islands == 1

def test_count_island_extreme_case_1K():
    map = read_map_from_file("tests/map_extreme_1K.txt")
    m = Map(map)
    n_islands = m.count_islands()
    
    assert n_islands == 1
    
def test_count_island_extreme_case_10K():
    map = read_map_from_file("tests/map_extreme_10K.txt")
    m = Map(map)
    n_islands = m.count_islands()
    
    assert n_islands == 1
    
def test_count_island_extreme_case_100K():
    map = read_map_from_file("tests/map_extreme_100K.txt")
    m = Map(map)
    n_islands = m.count_islands()
    
    assert n_islands == 1
    
def test_count_island_extreme_case_1M():
    map = read_map_from_file("tests/map_extreme_1M.txt")
    m = Map(map)
    n_islands = m.count_islands()
    
    assert n_islands == 1