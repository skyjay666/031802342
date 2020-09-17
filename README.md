## 软工第一次编程作业
 起初拿到题目是束手无措的，在参考了网上许多代码，有看到需多解法，最后还是选择了jaccard来解决对应题目
## 思路过程
Jaccard系数主要用于计算符号度量或布尔值度量的个体间的相似度，无法衡量差异具体值的大小，只能获得“是否相同”这个结果，所以Jaccard系数只关心个体间共同具有的特征是否一致这个问题。  
而且有看到同学成功使用，于是乎我也用这个。  
基本的方法还是和大家的大同小异，先使用jieba分词，在参考了其他人的代码后，先把文本处理只剩下汉字，然后再来分词。  
重要的函数部分是使用 Sklearn 库中的 CountVectorizer 来计算句子的 TF 矩阵，再利用 Numpy 来计算二者的交集和并集，随后计算杰卡德系数。  
"# SE031802342" 
