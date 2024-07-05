import sys
import re

def zz2():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    tihuan = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence)
    print(tihuan)

if __name__ == '__main__':
    zz2()
    sys.exit(0)