from gensim.models import Word2Vec

# 读取分词后的文本文件
with open('output.txt', 'r', encoding='utf-8') as f:
    sentences = [line.strip().split() for line in f]

# 初始化并训练模型
model = Word2Vec(sentences,
                 vector_size=100,  # 词向量维度
                 window=7,         # 上下文窗口大小
                 min_count=3,      # 忽略出现次数少于此值的单词
                 workers=4,        # 线程数量
                 sg=0,             # 使用skip-gram模型
                 hs=0,             # 不使用层次化softmax
                 negative=5,       # 使用负采样
                 epochs=30)        # 训练迭代次数

# 使用模型，例如获取单词的词向量
vector = model.wv['快递']
print(vector)

# 找到最相似的词
similar_words = model.wv.most_similar('快递', topn=5)
print(similar_words)

# 保存模型
model.save("word2vec.model")
