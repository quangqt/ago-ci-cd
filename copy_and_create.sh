#!/bin/bash

# input="./changed_files.txt"
files=`(git diff --name-only HEAD^ |grep "data/" && git ls-files -o  --exclude-standard | grep "data/")`
for file in $files; do
  mkdir -p "$(dirname "file_upload/$file")" && cp "$file" "file_upload/$file"
done
