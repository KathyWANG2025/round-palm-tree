import matplotlib.pyplot as plt
import math


x_value = list(range(1,100))
y_value = [math.sin(x) for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors=None, s=40)
plt.title("Square Numbers", fontsize = 8)
plt.xlabel("value", fontsize = 4)
plt.ylabel("square", fontsize = 4)

plt.show()
"""
import matplotlib.pyplot as plt

x_value = list(range(1, 100))
y_value = [x** 3 for x in x_value]  # 计算立方数

# 绘制散点图（使用蓝色系颜色映射，y值越大颜色越深）
plt.scatter(
    x_value,
    y_value,
    c=y_value,               # 根据y值确定颜色
    cmap=plt.cm.Blues,       # 使用蓝色系颜色映射
    edgecolors=None,         # 去除点的边缘
    s=40                    # 适当增大点的大小（从40调整为100）
)

# 设置图表标题和标签（修正标题文字，增大字体便于查看）
plt.title("Cube Numbers", fontsize=14)  # 标题改为"立方数"
plt.xlabel("Value", fontsize=12)        # x轴标签
plt.ylabel("Cube of Value", fontsize=12)# y轴标签明确为"值的立方"

# 显示颜色条（指示颜色对应的数值范围）
plt.colorbar(label='Cube Value')

plt.show()
"""