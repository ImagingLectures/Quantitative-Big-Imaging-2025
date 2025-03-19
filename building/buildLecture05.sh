jupyter-book build Lectures/Lecture-05 --builder pdflatex


gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=docs/QBI-Lecture05-AdvancedSegmentation.pdf Lectures/Lecture-05/_build/latex/QBI-Lecture05-AdvancedSegmentation.pdf 
