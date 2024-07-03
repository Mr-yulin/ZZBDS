import re
import sys

def zz1():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
    list = re.findall(pattern, sentence)
    print(list)
    print('--------华丽的分隔线--------')
    for i in pattern.finditer(sentence):
        print(i.group())
    print('--------华丽的分隔线--------')
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

if __name__ == '__main__':
    zz1()
    sys.exit(0)