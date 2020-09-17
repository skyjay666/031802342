import unittest
from jkd import jkdsim
import cha
base_data = open('sim0.8/orig.txt', 'r', encoding='utf-8').read()
text = {}
text['sim0.8\orig_0.8_add.txt'] = open('sim0.8/orig_0.8_add.txt', 'r', encoding='utf-8').read()
text['sim0.8\orig_0.8_del.txt'] = open('sim0.8\orig_0.8_del.txt', 'r', encoding='utf-8').read()
text['sim0.8\orig_0.8_dis_1.txt'] = open('sim0.8\orig_0.8_dis_1.txt', 'r', encoding='utf-8').read()
text['sim0.8\orig_0.8_dis_3.txt'] = open('sim0.8\orig_0.8_dis_3.txt', 'r', encoding='utf-8').read()
text['sim0.8\orig_0.8_dis_7.txt'] = open('sim0.8\orig_0.8_dis_7.txt', 'r', encoding='utf-8').read()
text['sim0.8\orig_0.8_dis_10.txt'] = open('sim0.8\orig_0.8_dis_10.txt', 'r', encoding='utf-8').read()
text['sim0.8\orig_0.8_dis_15.txt'] = open('sim0.8\orig_0.8_dis_15.txt', 'r', encoding='utf-8').read()
text['sim0.8\orig_0.8_mix.txt'] = open('sim0.8\orig_0.8_mix.txt', 'r', encoding='utf-8').read()
text['sim0.8\orig_0.8_rep.txt'] = open('sim0.8\orig_0.8_rep.txt', 'r', encoding='utf-8').read()

base_data1 = cha.change(base_data)


class AllTextGo(unittest.TestCase):

    def test_self_tfidf(self):
        print("Start")

        # base_data = open('sim0.8\orig.txt', 'r', encoding='UTF-8').read()
        # 新文件
        # new_data = open('sim0.8\orig_0.8_add.txt', 'r', encoding='UTF-8').read()
        # output = 'ans.txt'

        for key in text.keys():
            new_data1 = cha.change(text[key])
            result = jkdsim(base_data1, new_data1)
            print('相似度为：%.2f' %  result)
        print("End")


if __name__ == '__main__':
    unittest.main()
