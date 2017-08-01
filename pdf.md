# merge pdf files
* fast and small size: pdfunite xxx*.pdf output.pdf
* slow and big size: convert xxx*.pdf output.pdf

# convert images to pdf
* convert *.jpg output.pdf
* convert -density 960x750 -units PixelsPerInch *.jpg output.pdf

# resize all files in the current directory
for i in *; do eacho $i; convert $i -resize 50% $i; done
