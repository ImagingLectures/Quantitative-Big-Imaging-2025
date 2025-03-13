jupyter-book build Lectures/Lecture-04 --builder pdflatex

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=docs/QBI-Lecture04-BasicSegmentation.pdf Lectures/Lecture-04/_build/latex/QBI-Lecture04-BasicSegmentation.pdf
