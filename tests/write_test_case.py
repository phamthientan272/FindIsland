def write_extreme_test_case(file_path, n_rows, n_cols):
    with open(file_path, "w") as f:
        for i in range(n_rows):
            row = "1" * n_cols + "\n"
            f.write(row)

# Example usage:
# write_extreme_test_case("extreme_test_case.txt", 10000, 10000)
write_extreme_test_case("map_extreme_10K.txt", 100, 100)

