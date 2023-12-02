#!/bin/bash

input_image="DeepSea.jpg"      # Replace with your input image
zip_file="1000.zip"           # Replace with your ZIP file
output_image="DeepDiveDiscovery.jpg"   # Replace with your output image

# Concatenate the image and ZIP file
cat "$input_image" "$zip_file" > "$output_image"
