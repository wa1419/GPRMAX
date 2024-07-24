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
                    value = float(line)  # 转换为浮点数
                    data.append(value)
                except ValueError:
                    print(f"无法将行 '{line}' 转换为浮点数。")
    return data

def plot_data(data):
    """
    绘制数据图像。

    参数:
    data (list): 数据列表。
    """
    x = np.arange(len(data))  # 横坐标为数字的索引
    plt.figure(figsize=(10, 6))
    plt.plot(x, data, 'b-', label='Data')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Data Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

# 读取数据并绘图
# file_path = r"D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\out2txt\newGang1..txt"
file_path = r"D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\对比试验\ZhuTie2505.txt"
# file_path = r"D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\out2txt\newGang2..txt"
numeric_data = load_data(file_path)
plot_data(numeric_data)
