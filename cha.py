
#file = open('testc.txt', 'r', encoding='utf-8').read()
def change(file):
    def is_chinese(uchar):
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            return True
        else:
            return False
    str = ''
    for char in file:
        if is_chinese(char):
            str = str + char
    return str

#print(change(file))

