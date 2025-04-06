jupyter-book build Lectures/Lecture-08 --builder pdflatex

# cp Lectures/Lecture-08/_build/latex/QBI-Lecture08-Statistics.pdf docs/
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=docs/QBI-Lecture08-Statistics.pdf Lectures/Lecture-08/_build/latex/QBI-Lecture08-Statistics.pdf
