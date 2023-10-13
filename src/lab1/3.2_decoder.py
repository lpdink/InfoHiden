"""
实验3.2 LSB顺序隐写，解码器，输入带有信息的图像，信息的二进制长度，输出信息
"""
from pathlib import Path
import numpy as np
from PIL import Image

TEXT_LENGTH = 144 # 信息的二进制长度

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

def decode_bin_list(binary_list):
    binary_list = ["".join([str(num) for num in binary_list[i:i+8]]) for i in range(0,len(binary_list),8)]
    bytes_object = bytes([int(binary_string, 2) for binary_string in binary_list])
    decoded_string = bytes_object.decode('utf-8')
    return decoded_string

def decode(img_data, text_length):
    img_data = img_data.reshape(-1)
    # 提取img data 前text_length位的LSB位
    secret_part = img_data[:text_length]
    data = np.bitwise_and(secret_part, 1)
    data = np.bitwise_or(data, 0)
    return decode_bin_list(data)


def main():
    root_path = Path(__file__).parent.parent.parent
    resources = root_path/"resources"
    img_data = read_image(resources/"lab1"/"whu_with_secret.png")
    print(f"解密结果是：{decode(img_data, TEXT_LENGTH)}")

if __name__=="__main__":
    main()