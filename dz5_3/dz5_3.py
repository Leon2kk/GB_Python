# Семинар 5.
# Задание № 3.

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import os
os.system('cls') # чистим консоль

def encode(text):
	text_enc = ""
	i = 0
	while i < len(text):		
		cnt = 1
		while i + 1 < len(text) and text[i] == text[i + 1]:
			cnt += 1
			i += 1		
		text_enc += str(cnt) + text[i]
		i = i + 1
	return text_enc


def dencode(text:str):
    cnt = ""
    text_dec = ""
    for c in text:
        if c.isdigit():
            cnt += c
        else:
            text_dec += c * int(cnt)
            cnt = ''
    return text_dec

text_source = ''

# or input
with open('dz5_3\input.txt', 'r') as data:
    text_source = data.read()
data.close()

text_encode = encode(text_source)

#output
with  open('dz5_3\output.txt', 'w') as data:
    data.write(text_encode)
data.close()

text_dencode = dencode(text_encode)

print(text_source)
print(text_encode)
print(text_dencode)