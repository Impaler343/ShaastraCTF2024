#!/bin/bash

# Create the initial directory and put the text file in it
mkdir 1
cp insider.txt 1/

# Zip the initial directory
zip -r 1.zip 1
rm -r 1

for i in {2..1000}; do
	mkdir $i
	a=$((i-1))
	cp $a.zip $i/
	zip -r $i.zip $i
	rm -r $i
	rm -r $a.zip
done
