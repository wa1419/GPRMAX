import numpy as np


def generate_numbers(mean, variance, num_numbers):
    # 根据方差计算标准差
    std_deviation = np.sqrt(variance)

    # 生成11个随机数，使其均值为mean，方差为variance
    random_numbers = np.random.normal(loc=mean, scale=std_deviation, size=num_numbers)

    # 打印生成的数字
    for i, num in enumerate(random_numbers):
        print(f"#material: {num:.3f} 0.003 1.0 0.0 luji{i + 1}")



# 输入参数
mean_value = float(input("请输入均值（例如12）："))
variance_value = 0.2
num_numbers = 11

# 调用函数生成数字
generate_numbers(mean_value, variance_value, num_numbers)
