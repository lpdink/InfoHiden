"""
实验3.2 LSB顺序隐写，编码器，输入载体图像，信息，输出隐写后的图像
"""
from pathlib import Path
import numpy as np
from PIL import Image
from copy import deepcopy

SECRET = "原神，启动！"

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

def change_lsb(img_data, bin_msg):
    """按照信息的01序列改写图像矩阵的LSB

    Args:
        img_data (np.array): 载体图像矩阵
        bin_msg (list): 信息的0/1序列

    Returns:
        np.array: 含有信息的图像矩阵
    """
    assert img_data.size >= len(bin_msg), "载体过小，不足以承载信息信息"
    bin_msg = np.array(bin_msg, dtype=np.uint8)
    rst = deepcopy(img_data).reshape(-1)
    secret_part = rst[:bin_msg.size]
    rest_part = rst[bin_msg.size:]
    secret_part = np.bitwise_and(secret_part, 254)
    secret_part = np.bitwise_or(secret_part, bin_msg)
    rst = np.concatenate([secret_part, rest_part])
    # breakpoint()
    return rst.reshape(img_data.shape)

def encode_text(text):
    """将输入字符串转换为它的0/1表示

    Args:
        text (str): 待隐写信息

    Returns:
        list: 信息对应的0/1列表
    """
    bytes_object = text.encode('utf-8')
    binary_list = [format(byte, '08b') for byte in bytes_object]
    binary_list = [int(num) for nums in binary_list for num in nums]
    return binary_list

def main():
    root_path = Path(__file__).parent.parent.parent
    resources = root_path/"resources"

    secret_bin_seq = encode_text(SECRET)
    print(f"信息的二进制长度是:{len(secret_bin_seq)}，解密时使用这个长度.")
    img_data = read_image(resources/"whu.png")
    img_with_secret = change_lsb(img_data, secret_bin_seq)
    save_image(resources/"lab1"/"whu_with_secret.png",img_with_secret)
    pass

if __name__=="__main__":
    main()