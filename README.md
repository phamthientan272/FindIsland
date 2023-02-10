# Count islands
This application counts the number of island from a given path to the file that denotes a 2D array which visualize a map. Each elements of the array is either 0 (water) or 1 (land).

To run the application,
> cd app \
python main.py <path-to-file>

This repo also contains the bash script to build and run the docker file.
To run the application from the bash script:
> ./count_islands.sh \<path-to-file>

The tests case cover:
- all 0
- has 3 islands
- has 4 islands
- all 1 (1K, 10K, 100K, 1M cell)
- valid input (0, 1, and end-of-line)
- invalid input (other character)
- empty file
- non-existent file

The project also implements CI/CD pipeline that will trigger the github Action run all the tests case when push to main branch.