text = str(input('text:'))
key =  str(input('key:'))
# cipher_text = ''
byte = []
def xor(text,key):
	i = 0
	for char in text:
		xored_char = ord(char)^ord(key[i])
		byte.append(xored_char)
		i = i+1
		if i==len(key):
			i=0
def converting_hex():
	cipher_text = ''
	for i in byte:
		in_hex = hex(i)
		cipher_text = cipher_text + in_hex
	print('cipher_text:',cipher_text)

xor(text,key)
converting_hex()
# print(cipher_text)
# 	hex_text = hex(int(text,base=16))
# 	hex_key = hex(int(key,base=16))
