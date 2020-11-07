"""
python 实现异或加密
"""
import random
import re
from bitarray import bitarray


def writeinfile_1(thing):
    try:
        f = open('密文.txt', 'w', encoding='utf-8')
        f.write(thing)
        f.close()
        print("成功将'"+thing+"'存放在'密文.txt'\n")
    except IOError:
        print("写入文件失败")


def writeinfile_2(thing):
    try:
        f = open('明文.txt', 'w', encoding='utf-8')
        f.write(thing)
        f.close()
        print("成功将'"+thing+"'存放在'明文.txt'\n")
    except IOError:
        print("写入文件失败")


# 加密算法
def xor_enc(m, key):
    random.seed(key)  # 先存储密钥的种子
    key = random.randint(0,30000)
    print(key)
    #print('生成的密钥：'+str(random.randint(0, 99999)))
    #print('生成的密钥：' + str(random.randint(0, 99999)))
    #print('生成的密钥：' + str(random.randint(0, 99999)))
    #print(ord(key[0]))

    str_encode = ""
    str1 =""
    for i in m:
        str_encode += str(ord(i) ^ key) + ","
        str1 += chr(ord(i) ^ key)
    str_encode = str_encode.strip(",")
    print(str1)
    return str1


# 解码算法
def xor_dec(c, key):
    random.seed(key)  # 还是保存密钥种子
    key = random.randint(0,30000)
    print('生成数字密钥：'+str(key))
    str_decode = ""
    #print(random.randint(0,99999))
    for i in c.split(","):
        i = int(i)
        str_decode += chr(i ^ int(key))  # 异或解密
    return str_decode


if __name__ == '__main__':
    while True:
        print("*一个实现异或加密小程序*")
        print("---只能纯中文或者英文---")
        print("1.开始异或加密")
        print("2.开始异或解密")
        print("3.退出")
        choice = input()

        if choice == '1':
            m = input('输入明文：')
            key = input('输入密钥：')
            c = xor_enc(m, key)  # 返回的是一个二进制数字的字符串
            writeinfile_1(c)
            print("加密的结果为：" + c.replace(',', ''))

        elif choice == '2':
            c = input('输入密文：')
            key = input('输入密钥：')
            m = xor_dec(c, key)
            writeinfile_2(m)
            print("解密的结果为：" + m)

        elif choice == '3':
            print("结束")
            break
