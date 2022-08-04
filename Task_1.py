# Напишите программу, удаляющую из текста все слова, содержащие "абв"

text_in = input('Enter your text:\n ').split()
comb_lettr = input('Enter your combination of letters:\n ')
text_out = ' '.join([i for i in text_in if comb_lettr not in i])
print('Your text without this combination:\n', text_out)
