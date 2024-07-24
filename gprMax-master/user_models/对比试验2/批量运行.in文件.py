import os

def run_gprMax_for_in_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".in"):
            full_path = os.path.join(directory, filename)
            command = f"python -m gprMax {full_path} -n 1"
            os.system(command)
            print(f"运行了命令：{command}")

if __name__ == "__main__":
    input_directory = "D:\\Dpanfilefoder\\pythonProject\\gprMax-master\\user_models\\对比试验2"  # 指定你的文件夹路径
    run_gprMax_for_in_files(input_directory)
