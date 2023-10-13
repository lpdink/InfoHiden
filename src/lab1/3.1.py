"""
实验3.1
读取一张三通道RGB的png图像，将LSB或MSB清0，保存。

"""
from pathlib import Path
import numpy as np
from PIL import Image


def read_image(path):
    """读取图像

    Args:
        path (str): 图像路径

    Returns:
        np.array: 图像的像素矩阵
    """
    return np.array(Image.open(path))

def save_image(path, img_data):
    """保存图像

    Args:
        path (str): 保存图像的路径
        img_data (np.array): 图像的像素矩阵
    """
    img = Image.fromarray(img_data)
    img.save(path)

def change_lsb(img_data):
    """改变图像矩阵的LSB位为0

    Args:
        img_data (np.array): 图像矩阵

    Returns:
        np.array: 改变后的图像矩阵
    """
    return np.bitwise_and(img_data, 254)

def change_msb(img_data):
    """改变图像的MSB位为0

    Args:
        img_data (np.array): 图像矩阵

    Returns:
        np.array: 改变后的图像矩阵
    """
    return np.bitwise_and(img_data, 128)

def main():
    root_path = Path(__file__).parent.parent.parent
    resources = root_path/"resources"
    img_data = read_image(resources/"whu.png")
    lsb_ = change_lsb(img_data)
    msb_ = change_msb(img_data)
    save_image(resources/"lab1"/"whu_lsb.png", lsb_)
    save_image(resources/"lab1"/"whu_msb.png", msb_)

if __name__=="__main__":
    main()