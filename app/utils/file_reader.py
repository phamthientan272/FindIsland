def read_map_from_file(file_path):
    map = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            row = [int(x) for x in line.strip()]
            map.append(row)
    return map
