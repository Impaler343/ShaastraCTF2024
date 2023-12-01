#!/bin/bash

while [ $(find . -type f -name '*.zip' | wc -l) -gt 0 ]; do
    find . -type f -name "*.zip" -exec unzip -- '{}' \; -exec rm -- '{}' \;
    find . -type d -empty -delete
done
