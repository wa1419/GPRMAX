import numpy as np
import matplotlib.pyplot as plt

# 读取第一个.out文件的数据
data1 = np.loadtxt('user_models/try.out', encodings='utf-8',skiprows=3)  # 假设数据格式为文本，跳过前三行
Ez1 = data1[:, 0]  # 假设Ez数据在第一列
Hx1 = data1[:, 1]  # 假设Hx数据在第二列

# 读取第二个.out文件的数据
data2 = np.loadtxt('path_to_second_file.out', skiprows=3)  # 假设数据格式为文本，跳过前三行
Ez2 = data2[:, 0]  # 假设Ez数据在第一列
Hx2 = data2[:, 1]  # 假设Hx数据在第二列

# 创建图像
plt.figure()
plt.plot(Ez1, label='Ez1')
plt.plot(Ez2, label='Ez2')
plt.legend()
plt.title('Comparison of Ez from two files')

plt.figure()
plt.plot(Hx1, label='Hx1')
plt.plot(Hx2, label='Hx2')
plt.legend()
plt.title('Comparison of Hx from two files')

plt.show()
