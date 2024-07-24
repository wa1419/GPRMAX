import os
import shutil

# 源文件夹路径
source_folder = r"D:\Dpanfilefoder\pythonProject\gprMax-master\user_models\对比试验6(PVC)"
# 目标文件夹路径
target_folder = r"D:\gprshujvzhunbei\newdatasetcsv0714"

# 手动输入起始数字
start_number = int(input("请输入起始数字："))

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith(".csv"):
        # 判断文件名中是否包含特定关键词
        if "ZhuTie" in filename or "Tong" in filename:
            new_filename = f"metal{start_number}.csv"
        elif "PVC" in filename or "HNT" in filename:
            new_filename = f"pvc{start_number}.csv"
        else:
            # 如果没有特定关键词，保持原文件名
            new_filename = filename

        # 复制文件到目标文件夹
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, new_filename)
        shutil.copyfile(source_path, target_path)

        # 更新起始数字
        start_number += 1

print("CSV文件已成功复制到目标文件夹。")
