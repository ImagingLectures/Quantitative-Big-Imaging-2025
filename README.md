# Quantitative Big Imaging Course 2025

The course web page [is here](https://imaginglectures.github.io/Quantitative-Big-Imaging-2025).

## Installing pixi environment
### MacOS
Install the pixi enviroment
```
curl -fsSL https://pixi.sh/install.sh | sh
```

Install the dependencies
```
pixi install
pixi run pip install tensorflow-macos tensorflow-metal tensorflow-datasets```
pixi run jupyter-contrib-nbextension install --user
```

Run a jupyter notebook
```
pixi run jupyter-notebook
```
