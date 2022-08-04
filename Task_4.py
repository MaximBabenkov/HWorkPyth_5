# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# Входные и выходные данные хранятся в отдельных текстовых файлах

import os

def encode_RLE(data: str) -> str: 
	encoding = '' 
	prev_char = ''
	count = 1 
	if not data: return '' 
	for char in data: 
		if char != prev_char:
			if prev_char: 
				encoding += str(count) + prev_char
			count = 1 
			prev_char = char
		else: 
			count += 1 
	else: 
		encoding += str(count) + prev_char
		return encoding

path_1 = os.path.join('Folder', 'File_4_1.txt')
path_2 = os.path.join('Folder', 'File_4_2.txt')

with open (path_1, 'r') as f_1:
	data_to_encode = f_1.read()
print(data_to_encode)

coded = encode_RLE(data_to_encode)
print(coded)

with open (path_2, 'w') as f_2:
	f_2.write(coded)
print('This data is recorded to your file')

#-----------------------------------------------------------------#

def decode_RLE(data: str) -> str:
	decoding = '' 
	count = '' 
	for char in data: 
		if char.isdigit(): 
			count += char 
		else: 
			decoding += char * int(count) 
			count = ''
	return decoding

path_3 = os.path.join('Folder', 'File_4_3.txt')
path_4 = os.path.join('Folder', 'File_4_4.txt')

with open (path_3, 'r') as f_3:
	data_to_decode = f_3.read()
print(data_to_decode)

decoded = decode_RLE(data_to_decode)
print(decoded)

with open (path_4, 'w') as f_4:
	f_4.write(decoded)
print('This data is recorded to your file')
