import torch
import torch.backends.cudnn as cudnn
import numpy as np
import PIL.Image as pil_image
from util import convert_ycbcr_to_rgb, preprocess

def scaleup(model, img):

    cudnn.benchmark = True
    device = torch.device('cpu')

    image = img.convert('RGB')

    image_width = image.width * 4
    image_height = image.height * 4

    hr = image.resize((image_width, image_height), resample=pil_image.BICUBIC)
    lr = hr.resize((hr.width // 4, hr.height // 4), resample=pil_image.BICUBIC)
    bicubic = lr.resize((lr.width * 4, lr.height * 4), resample=pil_image.BICUBIC)

    lr, _ = preprocess(lr, device)
    hr, _ = preprocess(hr, device)
    _, ycbcr = preprocess(bicubic, device)

    with torch.no_grad():
        preds = model(lr).clamp(0.0, 1.0)

    preds = preds.mul(255.0).cpu().numpy().squeeze(0).squeeze(0)

    output = np.array([preds, ycbcr[..., 1], ycbcr[..., 2]]).transpose([1, 2, 0])
    output = np.clip(convert_ycbcr_to_rgb(output), 0.0, 255.0).astype(np.uint8)
    return output
