import sys
def read_map_from_file(file_path):
    map = []
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                row = [int(x) for x in line.strip()]
                map.append(row)
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error occured while reading file: {e}")
    
    if len(map) == 0:
        raise Exception("File is empty")
    return map
