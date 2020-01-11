# Dataset

Here's github for icon-adapter's code, which is a machine learning project. 

dataset and dataloader for machine learning project: icon processing

The icon dataset are extract from some themes from `zhuti.mi.com`.

## Download Data

Run `DownloadDataset.ipynb` using Jupyter Notebook.

## Prepare Data for MC-GAN 

Run `preprocess.py`, and uncomment the function you desire. Function `usecore()` uses `core.csv` to generate the core icons of all the themes, and transfers them to MC-GAN data (GlyphNet). Function `stackgan()` transfers any theme to MC-GAN data (OrnaNet).

## Prepare Data for Star-GAN

Run `toRaFD.py` to format the dataset to `RaFD` format for [StarGAN](https://github.com/yunjey/stargan).

## Other usage

If you want to use the dataset for other usage, we have `icon.py` or `icon_dataset.py` for you, which are 
two similar dataloaders for this dataset.

