# ml-icon-adapter

Here's github for icon-adapter's code, which is a machine learning project. 

dataset and dataloader for machine learning project: icon processing

# How to download anf format the icon dataset

The icon dataset are extract from some themes from `zhuti.mi.com`.

First run the code in `DownloadDataset.ipynb`, you will download the dataset 
into some where you like.

Then run `toRaFD.py` to format the dataset to `RaFD` format for [StarGAN](https://github.com/yunjey/stargan).

If you want to use the dataset for other usage, we have `icon.py` or `icon_dataset.py` for you, which are 
two similar dataloaders for this dataset.