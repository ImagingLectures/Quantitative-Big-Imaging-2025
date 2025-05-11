#!/bin/bash
# Usage: save as run-pytest.sh, make it executable

if command -v pixi &> /dev/null && pixi run which "jupyter-book" &> /dev/null; then
    pixi run jupyter-book build Lectures/Lecture-11 --builder pdflatex
else
    jupyter-book build Lectures/Lecture-11 --builder pdflatex
fi

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=docs/QBI-Lecture11-ScalingUp.pdf Lectures/Lecture-11/_build/latex/QBI-Lecture11-ScalingUp.pdf
