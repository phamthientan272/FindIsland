import sys
import argparse
from algo.island_counter import Map
from utils.file_reader import read_map_from_file


def main(args):
    try:
        map = read_map_from_file(args.file)
    except Exception as e:
        raise Exception("Error reading map file")
    m = Map(map)
    n_islands = m.count_islands()
    print(n_islands)     

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program to count number of islands in a map.')
    parser.add_argument("-f", "--file", type=str, help="Path to the file containing the map.", required=True)
    args = parser.parse_args()
    main(args)