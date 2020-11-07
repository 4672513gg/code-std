
import random

# 加密算法
def encodeStr(c, key):

	random.seed(key)  # 先存储密钥的种子
	str_encode = ""
	for i in c:

		str_encode += str(ord(i) ^ random.randint(0, 255)) + ","  # 异或加密，ord是将字符转化成asica对应的数字
		print(ord(i))
	str_encode = str_encode.strip(",")  # 去掉头和尾的，
	return str_encode

# 解码算法
def decodeStr(m, key):

	random.seed(key)  # 还是保存密钥种子
	str_decode = ""
	for i in m.split(","):

		i = int(i)
		str_decode += chr(i ^ random.randint(0, 255))  # chr是将字符转化成asica对应的字符
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