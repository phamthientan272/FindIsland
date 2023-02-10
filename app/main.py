from algo.island_counter import Map
from utils.file_reader import read_map_from_file
import sys

if __name__ == "__main__":
    try:
        map = read_map_from_file("../tests/map_empty.txt")
    except Exception as e:
        raise Exception("Error reading map file")
    
    print(len(map), len(map[0]), len(map)*len(map[0]))
    m = Map(map)
    n_islands = m.count_islands()
    print(n_islands)     