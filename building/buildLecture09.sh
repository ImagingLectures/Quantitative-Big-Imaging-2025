jupyter-book build Lectures/Lecture-09 --builder pdflatex

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=docs/QBI-Lecture09-DynamicExperiments.pdf Lectures/Lecture-09/_build/latex/QBI-Lecture09-DynamicExperiments.pdf
# cp Lectures/Lecture-09/_build/latex/QBI-Lecture09-DynamicExperiments.pdf docs/
