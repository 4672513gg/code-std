"""
python 实现异或加密
"""
import random


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
    random.seed(key)
    key = random.randint(0,99999)
    print(key)


    strin = ""
    for i in m:

        strin += chr(ord(i) ^ key) + ","
    strin = strin.strip(",")
    print(strin)

    return strin


# 解码算法
def xor_dec(c, key):
    random.seed(key)
    key = random.randint(0,99999)
    print('生成数字密钥：'+str(key))
    strin = ""

    for i in c.split(","):
        i = int(ord(i))
        strin += chr(i ^ int(key))  # 异或解密
    return strin


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
