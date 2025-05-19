# Quantitative Big Imaging Course 2025

The course web page [is here](https://imaginglectures.github.io/Quantitative-Big-Imaging-2025).

## Install the pixi environment manager
### Windows
Get the installer for the latest release at
```https://github.com/prefix-dev/pixi/releases/``` and run it. This is the better way than the powershell script recommended on the pixi.ch home page.

### MacOS
Install the pixi enviroment
```
curl -fsSL https://pixi.sh/install.sh | sh
```

## Install the lecture environment
Install the dependencies
```
pixi install
pixi run jupyter-contrib-nbextension install --user
```
### Install Tensorflow
Tensorflow requires GPU support. This differs between MacOS (uses Metal) and Windows/Linux (Uses Cuda).

#### For MacOS
```
pixi run pip install tensorflow-macos tensorflow-metal tensorflow-datasets```
```

## Run a jupyter notebook
To run jupyter notebook you need to start a terminal and type
```
pixi run jupyter-notebook
```


