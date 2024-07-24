# 帮我写一段python代码第一步以此文件为基础D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\对比试验2\ZhuTie(2.0-2.2加了jiceng)x=1.0y=0.5.in
# 读取其中的内容，只修改最后两行的内容
# 最后两行的内容是这样的
# #cylinder: 1.0 0.5 0 0.5 1.0 0.0025 0.25 ZhuTie
# #cylinder: 1.0 0.5 0 0.5 1.0 0.0025 0.2 free_space
# 我想只修改 #cylinder: 后边的七个数字中的第二个数和第四个 从0.5  0.6  0.7  .... 一直到1.5  第二个参数和第四个参数同时变化
# # 而且这个参数值决定了文件名D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\对比试验2\ZhuTie(2.0-2.2加了jiceng)x=1.0y=0.5  y=0.5这个位置的参数
# 修改内容，形成新的.in文件

def modify_last_two_lines(filename, current_x):
    # 读取原始文件内容
    with open(filename, "r") as file:
        lines = file.readlines()

    # 修改最后两行
    lines[-2] = f"#cylinder: 1.0 {current_x:.1f} 0 1.0 {current_x:.1f} 0.0025 0.25 ZhuTie\n"
    lines[-1] = f"#cylinder: 1.0 {current_x:.1f} 0 1.0 {current_x:.1f} 0.0025 0.2 free_space\n"

    # 构建新的文件名
    new_filename = f"ZhuTie2.0-2.2加了jicengx=1.0y={current_x:.1f}.in"

    # 保存修改后的内容到新文件
    with open(new_filename, "w") as new_file:
        new_file.writelines(lines)

    print(f"已生成新文件：{new_filename}")

def modify_and_generate_files(base_filename, start_x, end_x, step):
    for x in range(int(start_x * 10), int((end_x + step) * 10), int(step * 10)):
        current_x = x / 10.0
        modify_last_two_lines(base_filename, current_x)

# 调用函数，传入原始文件名、起始 x 值、结束 x 值和步长
base_filename = "ZhuTie2.0-2.2加了jicengx=1.0y=0.5.in"
start_x = 0.5
end_x = 1.5
step = 0.1
modify_and_generate_files(base_filename, start_x, end_x, step)
