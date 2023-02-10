#!/bin/bash

# Get the path to the file as an argument
file_path=$1

# Check if the argument is passed
if [ -z "$file_path" ]; then
  echo "Please provide the path to the file as an argument."
  exit 1
fi

# Check if the file exists
if [ ! -f "$file_path" ]; then
  echo "File does not exist"
  exit 1
fi

# Get the file name from the path
file_name=$(basename $file_path)

image_name="count-islands"
# Check if image already exists
if [ -z "$(docker images | grep $image_name)" ]; then
  # Build the image if it doesn't exist
    docker build -t $image_name .
fi


# Run the Docker container and pass the file as an argument
docker run --rm -t -v $file_path:/app/$file_name $image_name python main.py $file_name
