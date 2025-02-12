from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
from gensim.models import Word2Vec
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

from sklearn.decomposition import PCA
# 读取分词后的文本数据
with open('output.txt', 'r', encoding='utf-8') as f:
    sentences = [line.strip().split() for line in f if line.strip()]

# 训练 Word2Vec 模型
model = Word2Vec(sentences, vector_size=100,
                 window=9, min_count=7,
                 workers=4, sg=0, hs=0,
                 negative=5, epochs=30)

# 定义函数将文档转换为向量
def document_vector(word2vec_model, doc):
    doc = [word for word in doc if word in word2vec_model.wv.key_to_index]
    return np.mean(word2vec_model.wv[doc], axis=0) if doc else np.zeros(word2vec_model.vector_size)

# 计算每个文档的向量表示
doc_vectors = np.array([document_vector(model, doc) for doc in sentences])

# 规范化文档向量
scaler = StandardScaler()
doc_vectors_scaled = scaler.fit_transform(doc_vectors)



# 假设 doc_vectors_scaled 是您已经规范化的文档向量



# 使用 t-SNE 进行降维
tsne = TSNE(n_components=2, random_state=42)
doc_vectors_scaled = tsne.fit_transform(doc_vectors_scaled)



# 肘部法则确定最佳聚类数
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(doc_vectors_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()


# 轮廓系数分析
silhouette_scores = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    labels = kmeans.fit_predict(doc_vectors_scaled)
    score = silhouette_score(doc_vectors_scaled, labels)
    silhouette_scores.append(score)
    print(score)

plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores)
plt.title('Silhouette Scores')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.grid(True)
plt.show()

# 0.40575
# 0.40724462

# 0.4137582  k=6 10 6

# 0.4066927 k=6 12 7