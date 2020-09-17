import jkd
import cha
import sys

if __name__ == '__main__':
    #原文件
    base_data = open(sys.argv[1], 'r', encoding='utf-8').read()
    #新文件
    new_data = open(sys.argv[2], 'r', encoding='utf-8').read()
    output = sys.argv[3]

    base_data = cha.change(base_data)
    new_data = cha.change(new_data)
    jkd.ans_out(output,base_data,new_data)
    print(0)