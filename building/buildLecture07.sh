unzip Lectures/Lecture-07/data/grains.npy.zip
unzip Lectures/Lecture-07/data/ws_grains.npy.zip
unzip Lectures/Lecture-07/data/Cropped_prediction_8bit.npy.zip

jupyter-book build Lectures/Lecture-07 --builder pdflatex

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=docs/QBI-Lecture07-ComplexShape.pdf Lectures/Lecture-07/_build/latex/QBI-Lecture07-ComplexShape.pdf