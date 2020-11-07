# @Author  : ShiRui

import random

def writeinfile_1(thing):
    try:
        f = open('密文.txt','w',encoding='utf-8')
        f.write(thing)
        f.close()
    except IOError:
        print("出现异常")

def encode(key):
    tmp = []
    for k in key:
        tmp.append(bin(ord(k)).replace('0b', ''))
    key = ''.join(tmp)
    return key
# 加密算法
def encodeStr(info, key):
	key = encode(key)
	eninfo = encode(info)
	str_encode = []
	print(eninfo)
	print(key)
	for i in info:
		str_encode.append(str(ord(i)^int(key,2)))
		#str_encode += str(ord(i) ^ int(key, 2)) + ","  # 异或加密，ord是将字符转化成asica对应的数字


	#str_encode = str_encode.strip(",")  # 去掉头和尾的，
	print(str_encode[0:])
	#writeinfile_1(str_encode)
	return str_encode
# 解码算法
def decodeStr(info, key):

	#key = encode(key)
	str_decode = ""
	for i in info:
		print(i)
		i = encode(i)
		i = int(i) #1645339655,1645346275,1645343359
		str_decode += chr(i ^ int(key,2)%0x110000)  # chr是将字符转化成asica对应的字符
	return str_decode

if __name__ == '__main__':

	while(True):
		print("1.加密  2.解密  3.退出")
		num = input("请输入你选的选择：")
		if num == "1":

			info = input("请输入你要加密的内容:")
			key = input("请输入你的密钥：")
			str_encode = encodeStr(info, key)
			print(str_encode)

		elif num == "2":

			info = input("请输入你要解密的内容:")
			key = input("请输入你的密钥：")
			str_decode = decodeStr(info, key)
			print(str_decode)

		elif num == "3":
			break

		else:
			print("输入有误！")
