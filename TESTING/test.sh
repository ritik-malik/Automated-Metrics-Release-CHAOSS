#!/bin/bash

FOCUS_AREAS='focus_areas.tex'

echo "Focus area file found: ${FOCUS_AREAS}"

# copy the 'focus_areas.tex' file to a temp dir
mkdir -p temp
cp ${FOCUS_AREAS} temp
cd temp

# split the file based on delimiter
echo "Splitting the file into multiple files based on delimiter..."
csplit --digits=3 --prefix=outfile ${FOCUS_AREAS} "/\%DELIMITER/+1" "{*}"

# remove the original file
rm ${FOCUS_AREAS}

# delete empty files
echo "Deleting empty files"
find . -size 0 -delete

# traverse over output files and rename them
echo "Renaming focus_areas files..."
for FOCUS_AREA in outfile*
do
	FA=$(grep -F '%#' ${FOCUS_AREA} | awk '{print $NF}')
	mv ${FOCUS_AREA} ${FA}.tex
	echo "Making file ${FA}.tex"
done

mv * ..
cd ..
rmdir temp

echo "Done"
