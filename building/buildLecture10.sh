jupyter-book build Lectures/Lecture-10 --builder pdflatex

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=docs/QBI-Lecture10-BimodalExperiments.pdf Lectures/Lecture-10/_build/latex/QBI-Lecture10-BimodalExperiments.pdf

# cp Lectures/Lecture-10/_build/latex/QBI-Lecture10-BimodalExperiments.pdf docs/
