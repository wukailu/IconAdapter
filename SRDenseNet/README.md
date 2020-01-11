# SRDenseNet

## Train

For our project, simply put all the icons of all the themes under a single folder, and run `prepare.py` to create the dataset.

```bash
python train.py --train-file "xxx.h5" \
                --eval-file "yyy.h5" \
                --outputs-dir "zzz" \
                --lr 1e-4 \
                --batch-size 16 \
                --num-epochs 60 \
                --num-workers 8 \
                --seed 123                
```

## Test

```bash
python test.py --weights-file "xxx.pth" --image-file "yyy.bmp"
```
