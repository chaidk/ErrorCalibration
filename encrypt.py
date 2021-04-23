import numpy as np
import random

def encrypt(text, pwd, state):
        if text=='' or pwd=='':
            print('提示','待加密或解密，以及密码均不能为空。')
        else:
            if len(pwd)!=5:
                print('提示', '密码必须为5位阿拉伯数字。')
            else:
                try:
                    int(pwd)
                    M = np.array([[1, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 0],
                                  [0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 1]],
                                 dtype=int)
                    pwd = list(pwd)
                    for i in range(0, 4):
                        M[i][i] = pwd[i]
                    if state==1:
                        return text_encode(text, M)
                    if state==0:
                        return text_decode(text, M)
                except:
                    print('提示','密码必须为5位阿拉伯数字。')



def text_encode(text, M):
        # 将文本转化成列表
        text = list(text)
        Arr = []
        for k in text:
            if len(list(k.encode("unicode_escape"))) != 1:
                # 将每个汉字转化成Unicode编码
                res = k.encode("unicode_escape")
                # 将Unicode编码转化成ASCII编码
                res = list(res)[2:]
                res = [random.randint(1,1000)] + res
                narr = np.array(res, dtype=int)
                # 将ASCII代表的汉字乘以一个可逆矩阵
                r = np.matmul(narr, M)
                r = map(str, r)
                # 将数字列表转化成字符串
                r = ','.join(r)
            else:
                r = str(k)
            Arr.append(r)
        return ';'.join(Arr)+'。'

def text_decode(res, M):
    M_ = np.linalg.pinv(M)
    Arr = []
    if res.find('。') >= 0:
        res = res.split('。')
        res.remove('')
        res = ';'.join(res)
    res = res.split(';')
    for k in res:
        k = k.split(',')
        if len(k) !=1:
            k = np.array(k, dtype=int)
            r_ = np.matmul(k, M_)
            r_ = np.array(r_, dtype=int)
            text = bytes([92, 117]+list(r_)[1:]).decode('unicode_escape')
        else:
            text = str(k[0])
        Arr.append(text)
    return ''.join(Arr)


