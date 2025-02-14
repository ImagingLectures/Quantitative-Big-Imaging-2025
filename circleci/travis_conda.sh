# Configure the conda environment and put it in the path using the
# provided versions
conda env create -n book -f environment.yml
conda init zsh
source /home/travis/miniconda/etc/profile.d/conda.sh
conda activate book
pip install -U jupyter-book
pip install pyppeteer
python -c 'import pyppeteer; pyppeteer.chromium_downloader.download_chromium()'
pip install sphinxcontrib-bibtex
pip install webcolors
pip install itkwidgets
pip install plotly

# Kevins environment
# conda create -n testenv --yes python=$PYTHON_VERSION pip nose pytest
# conda env update -n testenv -f binder/environment.yml -q
# source activate testenv

# chmod a+x binder/postBuild
# sh binder/postBuild