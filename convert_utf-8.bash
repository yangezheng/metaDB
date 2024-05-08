#!/bin/bash

# Check if the user provided a directory as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Navigate to the provided directory
cd "$1" || exit 1

# Loop through each file in the directory
for file in *.csv; do
    if [ -f "$file" ]; then
        # Get the filename without the extension
        filename_without_extension="${file%.csv}"

        # Perform the iconv command to convert the file
        iconv -f WINDOWS-1252 -t UTF-8 "$file" > "utf-8_${filename_without_extension}.csv"
        echo "Converted $file to UTF-8 and saved as utf-8_${filename_without_extension}.csv"
    fi
done

echo "Conversion complete."

