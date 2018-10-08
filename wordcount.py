
def word_count(text_file):
	word_dict = {}
	with open(text_file) as file:
		# how to open file
		for line in file: 
			line = line.rstrip()
			words = line.split(" ")
			#print(words)
			for word in words:
				#manipulat word with strip to remove white space 
				word = word.strip(".,!/?-:123456789()!@#$%^^&*").lower()
				word_dict[word] = word_dict.get(word, 0) + 1
	#(word_dict.items())

	for key, value in word_dict.items():
		print(key, value)

	return word_dict

word_count("test.txt")


	
#print(word_count("test.txt")




# for key, value in my_dict.items():
#     print(f"key = {key}, value = {value}")