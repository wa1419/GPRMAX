import os
from gprMax.gprMax import api
import numpy as np
from tools.plot_Bscan import get_output_data, mpl_plot
from tools.outputfiles_merge import merge_files
import matplotlib.pyplot as plt
path = os.getcwd()  # 获得当前脚本所在的文件路径
for i in range(1,4):
    filename = str(i)+"th_model.in"
    f = open(filename, 'a')
    f.write("#title: the  {}th model\n".format(i))
    #保证模型的区域一致，便于做深度学习
    f.write("#domain: 8.4 14.4 0.02\n")
    #网格大小可以根据中心频率的需要进行调节
    f.write("#dx_dy_dz: 0.02 0.02 0.02\n")
    #时窗尽量保持一致
    f.write("#time_window: 50e-9\n")
    #材料可以设置为变化的
    f.write("#material: 6 0.01 1 0 car\n")
    #天线类型尽量保持一致，频率可以改变
    f.write("#waveform: ricker 1 100e6 my_ricker\n")
    #改变发射源的位置
    start_source_x=4.2
    start_source_y=0.2
    start_source_z=0
    source_x=start_source_x+i*0.5
    source_y=start_source_y+i*0.1
    source_z=start_source_z+i*0
    f.write("#hertzian_dipole: z {} {} {} my_ricker\n".format(source_x,source_y,source_z))
    #改变接收源的位置
    start_Rev_x=4.2
    start_Rev_y=0.75
    start_Rev_z=0
    Rev_x=start_Rev_x+i*0.5
    Rev_y=start_Rev_y+i+0.1
    Rev_z=start_Rev_z+i*0
    f.write("#rx: {} {} {}\n".format(Rev_x,Rev_y,Rev_z))
    #Bscan需要添加源移动步长和接收移动的步长
    step_source_x=0.02
    step_source_y=0
    step_source_z=0
    f.write("#src_steps: {} {} {}\n".format(step_source_x,step_source_y,step_source_z))
    step_Rev_x=0.02
    step_Rev_y=0
    step_Rev_z=0
    f.write("#rx_steps: {} {} {}\n".format(step_Rev_x,step_Rev_y,step_Rev_z))
    #模型可以根据需要进行改变,背景尽量设置为一个固定的，然后添加各种形状的异常
    f.write("#box: 0 0 0 8.4 14.4 0.02 car\n")
    f.write("#box: 4.7 11 0 6.7 12 0.02 free_space\n")
    f.write("#box: 4.7 6.5 0 5.7 7.5 0.02 free_space\n")
    f.write("#box: 4.7 2.5 0 5.2 3.5 0.02 free_space\n")
    #模型是否显示
    f.write("#geometry_view: 0 0 0 8.4 14.4 0.02 0.02 0.02 0.02 {} n \n".format(str(i)+"th_model"))
    #模型文件写完之后要关闭，免得影响后面的调用
    f.close()
    # 模型的运行
    api(filename, n=3, geometry_only=False)  # geometry_only：仅几何图形
    fi = filename[0:-3]
    merge_files(fi, removefiles=True)

    # 保存运行数据为txt，以及进行绘图保存
    filename_b = fi + '_merged.out'
    rxnumber = 1
    rxcomponent = 'Ez'
    # 获取回波数据
    outputdata, dt = get_output_data(filename_b, rxnumber, rxcomponent)
    # 保存回波数据
    fi2 = fi.split('/')[-1]  # 得到文件名，去掉了前面的路径
    out_path = path + '/out_data'
    if (os.path.exists(out_path)):
        pass
    else:
        os.mkdir(out_path)
    np.savetxt(out_path + '/' + fi2 + '.txt', outputdata, delimiter=' ')  # 未去除直达波

    # 绘图
    plt.imshow(outputdata, extent=[0, outputdata.shape[1], outputdata.shape[0], 0], interpolation='nearest',
               aspect='auto', cmap='gray',
               vmin=-np.amax(np.abs(outputdata)), vmax=np.amax(np.abs(outputdata)))
    img_path = path + '/img_data'
    if (os.path.exists(img_path)):
        pass
    else:
        os.mkdir(img_path)
    plt.savefig(img_path + '/' + fi2 + '.png', dpi=300)  # 保存图片