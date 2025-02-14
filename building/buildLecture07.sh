unzip Lectures/Lecture-07/data/grains.npy.zip
unzip Lectures/Lecture-07/data/ws_grains.npy.zip
unzip Lectures/Lecture-07/data/Cropped_prediction_8bit.npy.zip

jupyter-book build Lectures/Lecture-07 --builder pdflatex

cp Lectures/Lecture-07/_build/latex/QBI-Lecture07-ComplexShape.pdf docs/
