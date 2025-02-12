import re
import jieba


# 函数：读取停用词文件
def load_stopwords(filepath):
    stopwords = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.add(line.strip())
    return stopwords


# 函数：去除程度词
def remove_degree_words(text, degree_words):
    for word in degree_words:
        text = re.sub(r'\b{}\b'.format(word), '', text)
    return text


# 函数：清洗和分词
def preprocess_text(input_text, stopwords, degree_words):
    # 去除程度词
    text_without_degree_words = remove_degree_words(input_text, degree_words)

    # 去除特殊字符
    text_cleaned = re.sub(r'[^\w\s]', '', text_without_degree_words)

    # 分词
    words = jieba.cut(text_cleaned, cut_all=False)

    # 过滤停用词和程度词
    words_filtered = [word for word in words if word not in stopwords and word not in degree_words]

    return ' '.join(words_filtered)


# 主程序
if __name__ == '__main__':
    # 假设你的停用词列表在 'chinese_stopwords.txt' 文件中
    stopwords = load_stopwords('chinese_stopwords.txt')

    # 定义要去除的程度词列表
    degree_words = ["很", "还", "更加", "蛮", "确实", "更","都","挺"]

    # 读取文本文件
    with open('input1.txt', 'r', encoding='utf-8') as file:
        input_text = file.read()

    # 预处理文本
    processed_text = preprocess_text(input_text, stopwords, degree_words)

    # 输出到文本文件
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(processed_text)

    print("文本预处理完成，并已输出到 'output.txt'。")
