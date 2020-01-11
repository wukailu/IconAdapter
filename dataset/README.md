# Dataset

Here's github for icon-adapter's code, which is a machine learning project. 

dataset and dataloader for machine learning project: icon processing

## Download Data

Run `DownloadDataset.ipynb` using Jupyter Notebook.

## Process Data

Run `preprocess.py`, and uncomment the function you desire. Function `usecore()` uses `core.csv` to generate the core icons of all the themes, and transfers them to MC-GAN data (GlyphNet). Function `stackgan()` transfers any theme to MC-GAN data (OrnaNet).
=======
# How to download anf format the icon dataset

The icon dataset are extract from some themes from `zhuti.mi.com`.

First run the code in `DownloadDataset.ipynb`, you will download the dataset 
into some where you like.

Then run `toRaFD.py` to format the dataset to `RaFD` format for [StarGAN](https://github.com/yunjey/stargan).

If you want to use the dataset for other usage, we have `icon.py` or `icon_dataset.py` for you, which are 
two similar dataloaders for this dataset.

