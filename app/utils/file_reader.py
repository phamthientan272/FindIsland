import sys
def read_map_from_file(file_path):
    map = []
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                row = []
                for char in line.strip():
                    # Validate the file 
                    if char != '0' and char != '1':
                        raise Exception(f"Invalid character found: {char}")
                    else:
                        row.append(int(char))
                map.append(row)
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error occured while reading file: {e}")
    
    if len(map) == 0:
        raise Exception("File is empty")
    return map
