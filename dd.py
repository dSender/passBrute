alphabit = ['a', 'b', 'c']
alphabit_lenght = len(alphabit)

words_lenght = 3

all_words = len(alphabit) ** words_lenght

words = list()
for b in range(len(alphabit)):
	s = alphabit[b]
	word = [s] * words_lenght
	normalized_word = ''.join(word)
	words.append(normalized_word)
	k = 0
	while k != words_lenght:
		for i in range(words_lenght):
			if i != k:
				for m in range(len(alphabit)):
					word[i] = alphabit[m]
					normalized_word = ''.join(word)
					if normalized_word not in words:
						words.append(normalized_word)
					word = [s] * words_lenght
		k += 1
print(words)
print(len(words))


