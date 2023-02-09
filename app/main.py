from algo.island_counter import Map
from utils.file_reader import read_map_from_file

if __name__ == "__main__":
    map = read_map_from_file("../tests/map_extreme_10M.txt")
    print(len(map), len(map[0]), len(map)*len(map[0]))
    m = Map(map)
    n_islands = m.count_islands()
    print(n_islands)     