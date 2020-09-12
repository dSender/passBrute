
alphabit = ['a', 'd', 'm', 'i', 'n'] #  - input()
wordsLength = 6 # real words length - input()




def generator(alphabitToWords):
	def wrapper(alphabit, wordsLength):
		nwords = list()
		all_words = alphabitToWords(alphabit)
		for i in range(len(all_words)):
			for k in range(0, len(all_words)): 
				word_basement = all_words[i]
				word_brick = all_words[k]
				word = word_basement
				while len(word) < wordsLength:
					word = word + word_brick
				nword = word[0: wordsLength]
				if nword not in nwords:
					nwords.append(nword)
		return nwords
	return wrapper


@generator
def alphabitToWords(alphabit):
	alphabit_lenght = len(alphabit)
	words_length = 2

	"""
	 Then generates 		low-level words
	 				   ^
	 				   |
	 	using alphabit | and returns the list

	"""
	words = list() 					# List to return

	for b in range(len(alphabit)):
		s = alphabit[b]		
		word = [s] * words_length
		normalized_word = ''.join(word)
		words.append(normalized_word)
		k = 0
		while k != words_length:
			for i in range(words_length):
				if i != k:
					for m in range(len(alphabit)):
						word[i] = alphabit[m]
						normalized_word = ''.join(word)
						if normalized_word not in words:
							words.append(normalized_word)
						word = [s] * words_length
			k += 1
	return words

passwordWords = alphabitToWords(alphabit, wordsLength)

print(passwordWords)
