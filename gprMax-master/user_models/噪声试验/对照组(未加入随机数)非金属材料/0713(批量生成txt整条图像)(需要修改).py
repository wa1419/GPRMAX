import os
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_name):
    """
    从.txt文件中读取数据并转换为浮点数。

    参数:
    file_name (str): 文件名。

    返回:
    data (list): 包含所有数据的列表。
    """
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()  # 去掉换行符
            if line:  # 确保不是空行
                try:
                    # 按字符分割行并转换为浮点数
                    values = line.split()
                    for value in values:
                        data.append(float(value))
                except ValueError:
                    print(f"无法将行 '{line}' 转换为浮点数。")
    return data

def plot_data(data, file_name):
    """
    绘制数据图像并保存为同名图片。

    参数:
    data (list): 数据列表。
    file_name (str): 文件名。
    """
    x = np.arange(len(data))  # 横坐标为数字的索引
    plt.figure(figsize=(10, 6))
    plt.plot(x, data, 'b-', label='Data')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(file_name)  # 使用文件名作为图像标题
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{file_name}.png")  # 保存为同名图片
    plt.show()

# 遍历out2txt文件夹下的所有.txt文件
out2txt_folder = r"D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\噪声试验"
for txt_file in os.listdir(out2txt_folder):
    if txt_file.endswith(".txt"):
        file_path = os.path.join(out2txt_folder, txt_file)
        numeric_data = load_data(file_path)
        plot_data(numeric_data, os.path.splitext(txt_file)[0])  # 使用文件名（不包含扩展名）作为图片名
