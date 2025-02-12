import numpy as np
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

# 创建一个横向椭圆形遮罩
def create_ellipse_mask(width, height, center=None, axes=None):
    if center is None:  # 使用图片中心作为椭圆中心
        center = (int(width / 2), int(height / 2))
    if axes is None:  # 横向椭圆的长轴和短轴
        axes = (int(width / 2), int(height / 4))  # 修改这里来改变椭圆的形状

    y, x = np.ogrid[:height, :width]
    mask = ((y - center[1]) / axes[1]) ** 2 + ((x - center[0]) / axes[0]) ** 2 > 1
    mask = 255 * mask.astype(int)
    return mask

# 其余的代码保持不变...


    y, x = np.ogrid[:height, :width]
    mask = ((y - center[1]) / axes[1]) ** 2 + ((x - center[0]) / axes[0]) ** 2 > 1
    mask = 255 * mask.astype(int)
    return mask


# 设置遮罩的尺寸
mask_width = 800
mask_height = 800

# 创建遮罩
ellipse_mask = create_ellipse_mask(mask_width, mask_height)

# 读取文本数据
with open('output.txt', 'r', encoding='utf-8') as file:
    output_text = file.read()

# 清洗文本并分词
words = re.findall(r'\w+', output_text)

# 计算词频
word_counts = Counter(words)

# 输出最常见的10个单词
print(word_counts.most_common(20))

# 创建词云对象
wordcloud = WordCloud(font_path='simhei.ttf', width=mask_width, height=mask_height,
                      background_color='white', mask=ellipse_mask)

# 生成词云
wordcloud.generate_from_frequencies(word_counts)

# 绘制词云
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')  # 使用双线性插值显示更清晰的边界
plt.axis("off")
plt.tight_layout(pad=0)

# 显示图像
plt.show()
