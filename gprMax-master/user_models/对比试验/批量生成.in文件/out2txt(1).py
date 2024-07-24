import sys
import os
import numpy as np
from tools.plot_Bscan import get_output_data, mpl_plot
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# # 添加gprMax模块的路径
# sys.path.append('D:/GPR/gprmax/gprMax')

def mpl_plot(filename, outputdata, dt, rxnumber, rxcomponent):
    """
    使用Matplotlib绘制B扫描数据。

    参数:
    filename (str): 文件名。
    outputdata (ndarray): 要绘制的输出数据。
    dt (float): 时间步长。
    rxnumber (int): 接收器编号。
    rxcomponent (str): 接收器组件。
    epsilon_r (float): 相对介电常数。
    mu_r (float): 相对磁导率。
    c (float): 介质中的光速。

    返回:
    fig, ax: 图像和轴对象。
    """
    (path, filename) = os.path.split(filename)
    fig, ax = plt.subplots(figsize=(20, 10), facecolor='w', edgecolor='w')
    ax.set_title(filename + ' - rx' + str(rxnumber))

    im = ax.imshow(outputdata,
                   extent=[0, outputdata.shape[1], outputdata.shape[0] * dt, 0],
                   interpolation='nearest', aspect='auto', cmap='seismic',
                   vmin=-np.amax(np.abs(outputdata)), vmax=np.amax(np.abs(outputdata)))

    ax.set_xlabel('Trace number')
    ax.set_ylabel('Time [s]')
    ax.grid(which='both', axis='both', linestyle='-.')

    cb = plt.colorbar(im)
    if 'E' in rxcomponent:
        cb.set_label('Field strength [V/m]')
    elif 'H' in rxcomponent:
        cb.set_label('Field strength [A/m]')
    elif 'I' in rxcomponent:
        cb.set_label('Current [A]')

    c = 3e8  # 真空中的光速 (m/s)
    epsilon_r = 12  # 相对介电常数
    mu_r = 1  # 相对磁导率


    # # 计算深度
    # depth = c * (np.arange(outputdata.shape[0]) * dt) / (2 * np.sqrt(epsilon_r * mu_r))

    # 添加深度刻度
    secax = ax.secondary_yaxis('right', functions=(lambda x: c * x / (2 * np.sqrt(epsilon_r * mu_r)),
                                                   lambda x: 2 * x * np.sqrt(epsilon_r * mu_r) / c))
    secax.set_ylabel('Depth [m]')
    secax.grid(which='both', axis='both', linestyle='-.')

    width = np.arange(outputdata.shape[1]) * 0.02
    ax3 = ax.twiny()
    ax3.set_xlabel('Width [m]')
    ax3.set_xlim(ax.get_xlim())
    ax3.set_xticks(ax.get_xticks())
    ax3.set_xticklabels(['{:.2f}'.format(w) for w in np.linspace(width[0], width[-1], len(ax.get_xticks()))])

    return fig, ax

def mean_gpr(x):
    """
    通过减去每行的均值来去除GPR数据中的直达波。

    参数:
    x (ndarray): 输入数据。

    返回:
    x_new (ndarray): 去除直达波后的数据。
    """
    return x - np.mean(x, axis=1, keepdims=True)

def remove_direct_wave_images(outputdata, dt, threshold=10e-9):
    """
    移除时间标签小于1ns的图像，并对剩余图像进行强度自适应处理。

    参数:
    outputdata (ndarray): 输入数据。
    dt (float): 时间步长。
    threshold (float): 时间阈值，默认为1ns。

    返回:
    filtered_data (ndarray): 过滤后的数据。
    """
    time = np.arange(outputdata.shape[0]) * dt
    mask = time >= threshold
    filtered_data = outputdata[mask, :]
    return filtered_data

# 获取当前目录下的所有文件
files = os.listdir()

# 定义保存图像的文件夹
image_folder = './image'

# 确保image文件夹存在
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

for file in files:
    # if file.endswith("merged.out"):
    if file.endswith(".out"):
        filename_b = file
        rxnumber = 1
        rxcomponent = 'Ez'

        try:
            # 获取回波数据
            outputdata, dt = get_output_data(filename_b, rxnumber, rxcomponent)

            # 保存回波数据
            fi2 = file[:-3]
            np.savetxt(fi2 + 'txt', outputdata, delimiter=' ')

            # 绘制并显示未去直达波图像
            fig, ax = mpl_plot(filename_b, outputdata, dt, rxnumber, rxcomponent)
            plt.savefig(os.path.join(image_folder, fi2 + '.png'), dpi=300)

            # 去直达波
            x_s = mean_gpr(outputdata)

            # 绘制去直达波图像
            im_rm = ax.imshow(x_s, extent=[0, x_s.shape[1], dt * x_s.shape[0], 0],
                              aspect='auto', cmap='seismic',
                              vmin=-np.amax(np.abs(x_s)), vmax=np.amax(np.abs(x_s)))

            # 保存去直达波图像
            plt.savefig(os.path.join(image_folder, fi2 + '_RM.png'), dpi=300)

            # 移除时间标签小于1ns的图像，并进行强度自适应处理
            filtered_data = remove_direct_wave_images(outputdata, dt)
            fig, ax = mpl_plot(filename_b, filtered_data, dt, rxnumber, rxcomponent)
            plt.savefig(os.path.join(image_folder, 'R' + fi2 + '.png'), dpi=300)

        except Exception as e:
            print(f"处理文件 {file} 时出错: {e}")
