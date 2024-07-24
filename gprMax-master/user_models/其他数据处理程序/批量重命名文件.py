import os


def rename_txt_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # 获取文件的绝对路径
            file_path = os.path.join(root, filename)

            # 检查文件是否是 .txt 文件
            if filename.lower().endswith('.txt'):
                # 分割文件名，获取倒数第三个小数点之前的部分
                parts = filename.split('.')
                new_filename = '.'.join(parts[:-3]) + '.' + parts[-1]

                # 重命名文件
                new_file_path = os.path.join(root, new_filename)
                os.rename(file_path, new_file_path)
                print(f"重命名文件：{filename} -> {new_filename}")


# 指定要遍历的文件夹路径
folder_path = r'D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\对比试验3'
rename_txt_files(folder_path)
