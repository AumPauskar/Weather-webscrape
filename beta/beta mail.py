file = open('textfile.txt', 'r')
document = file.read()
temp = ''
for a in range(len(document)):
	if document[a] == 'º' or document[a] == 'Â':
		print('baba booyah')
	else:
		temp += document[a]
print(document)
print(temp)