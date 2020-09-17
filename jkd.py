import jieba
import numpy
from sklearn.feature_extraction.text import CountVectorizer



# jieba分词
def add_space(s):
    result = jieba.cut(s, cut_all=True)
    return ' '.join(list(result))

# 求杰卡德相似度
def jkdsim(s0, s1):
    s0, s1 = add_space(s0), add_space(s1)
    #用sklearn的CountVectorizer使文本的词语转换为词频矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    #语料库
    corpus = [s0, s1]
    #使用fit_transform函数计算各个词语出现的次数
    vectors = cv.fit_transform(corpus).toarray()
    #并集
    denominator = numpy.sum(numpy.max(vectors, axis=0))
    #交集
    numerator = numpy.sum(numpy.min(vectors, axis=0))
    #计算杰卡德相似指数
    return 1.0 * numerator / denominator

# 计算相似度并写入文件
def ans_out(output, file, test):
    with open(output, 'a') as file_handle:
        # 方便下次写入清空
        file_handle.truncate(0)
        file_handle.write('%.2f' %jkdsim(file, test))
        file_handle.close()