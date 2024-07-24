# 定义初始参数
y1 = 2.2
y2_increment = 0.01

# 循环遍历 y1 的范围
for i in range(1, 16):  # 15次循环，对应 y1 从 2.2 到 2.35
    y2 = round(y1 + y2_increment, 2)  # 使用 round 函数保留两位小数
    y1 = round(y1,2)

    # 判断计数的单双
    if i % 2 == 1:  # 单数
        print(f"#box: 0.0 {y1} 0.0 3.5 {y2} 0.0025 liqing")
    else:  # 双数
        print(f"#box: 0.0 {y1} 0.0 3.5 {y2} 0.0025 jiceng")

    # 更新 y1 的值
    y1 += y2_increment
