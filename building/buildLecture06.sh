jupyter-book build Lectures/Lecture-06 --builder pdflatex

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=docs/QBI-Lecture06-ShapeAnalysis.pdf Lectures/Lecture-06/_build/latex/QBI-Lecture06-ShapeAnalysis.pdf 
