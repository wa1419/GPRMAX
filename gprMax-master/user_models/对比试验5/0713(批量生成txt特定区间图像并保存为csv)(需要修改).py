import os
import numpy as np
import matplotlib.pyplot as plt

# 定义区间范围字典
range_dict = {
    5: (6000, 8000),
    6: (5500, 7500),
    7: (5000, 7000),
    8: (4500, 6500),
    9: (4300, 6300),
    10: (4000, 6000),
    11: (3500, 5500),
    12: (3000, 5000),
    13: (2800, 4800),
    14: (2500, 4500),
    15: (2000, 4000),
    16: (1600, 3600),
    17: (1350, 3350),
    18: (1200, 3200)
}

def load_data(file_name):
    # 从.txt文件中读取数据并转换为浮点数。
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
    # 绘制数据图像并保存为同名图片。
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

# 文件夹路径
out2txt_folder = r"D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\对比试验5"

# 遍历out2txt文件夹下的所有.txt文件
for txt_file in os.listdir(out2txt_folder):
    if txt_file.endswith(".txt"):
        try:
            # 提取最后两位数字
            last_two_digits = int(txt_file[-6:-4])
        except ValueError:
            # 如果提取失败（不是数字），跳过该文件
            print(f"跳过文件：{txt_file}，因为文件名后两位不是数字。")
            continue

        file_path = os.path.join(out2txt_folder, txt_file)
        numeric_data = load_data(file_path)

        if last_two_digits in range_dict:
            # 如果匹配成功，只保留和字典匹配的数据范围
            lower, upper = range_dict[last_two_digits]
            selected_data = numeric_data[lower:upper]
            # plot_data(selected_data, f"{os.path.splitext(txt_file)[0]}_select")

            # 将匹配的数据保存为同名的csv文件
            csv_file_name = f"{os.path.splitext(txt_file)[0]}_{last_two_digits}.csv"
            np.savetxt(csv_file_name, selected_data, delimiter=',')
        else:
            # 如果匹配失败，绘制整条数据并保存为图片
            plot_data(numeric_data, os.path.splitext(txt_file)[0])
