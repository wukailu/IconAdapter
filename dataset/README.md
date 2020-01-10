# Dataset

Here's github for icon-adapter's code, which is a machine learning project. 

dataset and dataloader for machine learning project: icon processing

## Download Data

Run `DownloadDataset.ipynb` using Jupyter Notebook.

## Process Data

Run `preprocess.py`, and uncomment the function you desire. Function `usecore()` uses `core.csv` to generate the core icons of all the themes, and transfers them to MC-GAN data (GlyphNet). Function `stackgan()` transfers any theme to MC-GAN data (OrnaNet).
