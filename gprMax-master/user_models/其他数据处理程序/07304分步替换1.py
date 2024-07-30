import os

# 定义文件路径
base_path = r'D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\5×2×14×3×2\2×8×2×3×14\0101010101\01'
input_file_path = os.path.join(base_path, '0101010101.in')

# 定义新的文件名和对应的替换内容
new_files = {
    '01': ('#material: 500 10000000.0 1.0 0.0 ZhuTie\n', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 ZhuTie\n'),
    '02': ('#material: 500 60000000.0 1.0 0.0 Tong\n', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 Tong\n'),
    '03': ('#material: 500 1000000.0 1.0 0.0 TanGang\n', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 TanGang\n'),
    '04': ('#material: 500 1500000.0 1.0 0.0 BuXiuGang\n', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 BuXiuGang\n'),
    '05': ('#material: 4 0.01 1.0 0.0 PVC\n', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 PVC\n'),
    '06': ('#material: 10 0.05 1.0 0.0 HNT\n', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 HNT\n'),
    '07': ('#material: 2.5 0.000000000000000001 1.0 0.0 PE\n', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 PE\n'),
    '08': ('#material: 8 0.000000000001 1.0 0.0 TaoCi\n', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 TaoCi\n')
}

# 定义五六位的替换内容
additional_modifications = {
    '01': ('#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.11 ', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.1 free_space\n'),
    '02': ('#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.25 ', '#cylinder: 1.0 0.5 0 1.0 0.5 0.0025 0.2 free_space\n')
}

# 定义七八位的替换内容
final_modifications = {
    '01': ('#hertzian_dipole: z 0.96 2.48 0.0 mysource\n', '#rx: 1.01 2.48 0.0\n'),
    '02': ('#hertzian_dipole: z 0.98 2.48 0.0 mysource\n', '#rx: 1.03 2.48 0.0\n'),
    '03': ('#hertzian_dipole: z 1.0 2.48 0.0 mysource\n', '#rx: 1.05 2.48 0.0\n')
}

# 定义九十位的替换内容
depth_modifications = {
    '01': '0.5', '02': '0.6', '03': '0.7', '04': '0.8', '05': '0.9', '06': '1.0',
    '07': '1.1', '08': '1.2', '09': '1.3', '10': '1.4', '11': '1.5', '12': '1.6',
    '13': '1.7', '14': '1.8'
}

# 检查文件是否存在
if os.path.exists(input_file_path):
    # 读取文件内容
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 修改并保存为新文件（修改三四位）
    for key, (new_material, new_cylinder) in new_files.items():
        if len(lines) >= 39:
            lines[15] = new_material
            lines[38] = new_cylinder

        new_file = f'01{key}010101.in'
        output_file_path = os.path.join(base_path, new_file)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        print(f"文件已成功修改并保存为 {output_file_path}")

    # 遍历文件夹，修改五六位
    for file_name in os.listdir(base_path):
        if file_name.endswith('.in'):
            input_file_path = os.path.join(base_path, file_name)
            with open(input_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for case, (new_cylinder, new_free_space) in additional_modifications.items():
                if len(lines) >= 39:
                    lines[-2] = new_cylinder + new_files[file_name[2:4]][1].split()[-1] + '\n'
                    lines[-1] = new_free_space

                output_file_path = os.path.join(base_path, file_name[:4] + case + file_name[6:])
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.writelines(lines)

                print(f"文件已成功修改并保存为 {output_file_path}")

    # 遍历文件夹，修改七八位
    for file_name in os.listdir(base_path):
        if file_name.endswith('.in'):
            input_file_path = os.path.join(base_path, file_name)
            with open(input_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for final_case, (new_dipole, new_rx) in final_modifications.items():
                if len(lines) >= 6:
                    lines[5] = new_dipole
                    lines[6] = new_rx

                output_file_path = os.path.join(base_path, file_name[:6] + final_case + file_name[8:])
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.writelines(lines)

                print(f"文件已成功修改并保存为 {output_file_path}")

    # 遍历文件夹，修改九十位
    for file_name in os.listdir(base_path):
        if file_name.endswith('.in'):
            input_file_path = os.path.join(base_path, file_name)
            with open(input_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for depth_key, depth_value in depth_modifications.items():
                if len(lines) >= 39:
                    # 修改倒数第一行和倒数第二行的第二个和第五个参数
                    lines[-2] = lines[-2].split()
                    lines[-2][2] = depth_value
                    lines[-2][5] = depth_value
                    lines[-2] = ' '.join(lines[-2]) + '\n'

                    lines[-1] = lines[-1].split()
                    lines[-1][2] = depth_value
                    lines[-1][5] = depth_value
                    lines[-1] = ' '.join(lines[-1]) + '\n'

                output_file_path = os.path.join(base_path, file_name[:8] + depth_key + file_name[10:])
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.writelines(lines)

                print(f"文件已成功修改并保存为 {output_file_path}")
else:
    print(f"文件 {input_file_path} 不存在，请检查路径是否正确。")
