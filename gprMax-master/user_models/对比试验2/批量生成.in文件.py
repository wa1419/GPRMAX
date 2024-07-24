
def generate_cylinder_in_files(base_filename, start_x, end_x, step, output_directory):
    for x in range(int(start_x * 10), int((end_x + step) * 10), int(step * 10)):
        current_x = x / 10.0
        input_filename = f"{base_filename}x=1.0y=0.5.in"
        output_filename = f"{output_directory}/{base_filename}2.5{current_x:.1f}.in"

        with open(input_filename, "r") as input_file:
            lines = input_file.readlines()
            # 修改最后两行
            lines[-2] = f"#cylinder: 2.5 {current_x:.1f} 0 2.5 {current_x:.1f} 0.0025 0.25 ZhuTie\n"
            lines[-1] = f"#cylinder: 2.5 {current_x:.1f} 0 2.5 {current_x:.1f} 0.0025 0.2 free_space\n"

        with open(output_filename, "w") as output_file:
            output_file.writelines(lines)


if __name__ == "__main__":
    base_filename = "ZhuTie(2.0-2.2加了jiceng)x=1.0y=0.5.in"
    start_x = 0.5
    end_x = 1.5
    step = 0.1
    output_directory = "D:/Dpanfilefoder/pythonProject/gprMax-master/user_models/对比试验/批量生成.in文件"
    generate_cylinder_in_files(base_filename, start_x, end_x, step, output_directory)
    print(f"生成了 {(end_x - start_x) / step + 1} 个文件到 {output_directory} 目录下。")
