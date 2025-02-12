import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = 'C:\\Windows\\Fonts\\simhei.ttf'  # 修改为你的系统中的实际路径
font = FontProperties(fname=font_path, size=14)
font_t = FontProperties(fname=font_path, size=25)
# 读取CSV文件
df = pd.read_csv('price_buyer.csv')  # 更改为您的CSV文件路径

# 显示前几行数据以确认读取正确
print(df.head())

# 假设CSV文件中的列名为'price'和'num_purchases'
# 对价格进行基本统计分析
price_stats = df['price'].describe()
print("价格统计信息：")
print(price_stats)

# 对付款人数进行基本统计分析
purchase_stats = df['num_purchases'].describe()
print("付款人数统计信息：")
print(purchase_stats)

# 绘制价格的直方图
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, color='blue', edgecolor='black')
plt.title('商品价格分布', fontproperties=font_t)
plt.xlabel('价格',  fontproperties=font)
plt.ylabel('商品数', fontproperties=font)
plt.show()

# 绘制付款人数的直方图
plt.figure(figsize=(10, 6))
plt.hist(df['num_purchases'], bins=20, color='green', edgecolor='black')
plt.title('商品付款人数分布', fontproperties=font_t)
plt.xlabel('付款人数', fontproperties=font)
plt.ylabel('商品数', fontproperties=font)
plt.show()

# 可以进一步分析价格与付款人数之间的关系
plt.figure(figsize=(10, 6))
plt.scatter(df['price'], df['num_purchases'])
plt.title('价格与付款人数的关系', fontproperties=font_t)
plt.xlabel('价格', fontproperties=font)
plt.ylabel('付款人数', fontproperties=font)
plt.show()
