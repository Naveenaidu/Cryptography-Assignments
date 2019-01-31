import re

def monolithic_subtitution(input_file,output_file):
	"""
	Substitutes plain text letters with cipher text letters.
	Replaces each plain text letter with it's monolithic 
	substitution and writes it to the outputfile. 

	Ignores whitespace and all the special characters

	param
		
		input_file : The plaintext file 
		output_file: The file with the monolithic substitution

	alphabets: Dictionary where {'key':'value'} refers to
	           {'letter':'substitution-letter'}
	"""

	alphabets = {'a':'D', 'b':'E', 'c':'F', 'd':'G', 'e':'H',
	             'f':'I', 'g':'K', 'h':'J', 'i':'L', 'j':'M',
	             'k':'R', 'l':'Q', 'm':'P', 'n':'O', 'o':'N',
	             'p':'S', 'q':'T', 'r':'U', 's':'V', 't':'W',
	             'u':'X', 'v':'Y', 'w':'Z', 'x':'B', 'y':'A',
	             'z':'C'}

	while True:
		ch = input_file.read(1) #Reading file char by char
		if not ch: 
			input_file.close()
			output_file.close()
			return
		try:
			ch = ch.lower()
			cipher_letter = alphabets[ch]
			output_file.write(cipher_letter)
		except:
			continue	

def count_chars(cipher_file):
	"""
	Counts the occurences of each letter in the cipher text

	param:
		cipher_file: The file encrypted by monolithic substitution

	alphabets_count: Dictionary where {'key':'value'} refers to
	                 {'letter':'no-of-occurences'}	


	"""

	alphabets_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0,
	                   'F':0, 'G':0, 'H':0, 'I':0, 'J':0,
	                   'K':0, 'L':0, 'M':0, 'N':0, 'O':0,
	                   'P':0, 'Q':0, 'R':0, 'S':0, 'T':0,
	                   'U':0, 'V':0, 'W':0, 'X':0, 'Y':0,
	                   'Z':0}

	while True:
		ch = cipher_file.read(1) #Reading file char by char
		if not ch:
			break
		alphabets_count[ch]+= 1

	return(alphabets_count)

def count_n_graphs(cipher_file,length):
	"""
	Count the number of digraphs and trigraphs

	params:
		cipher_file: file with the cipher text
		length: The length of the string pattern

	pattern_count_dict: Dictionary which holds the pattern and
						the count of it's occurence in the file.						

	This function reads the file and starts making pairs/ 
	triplets string pattern from the first character.	   
	"""
	pattern_count_dict = {}

	text = cipher_file.readline()
	file_length = len(text)
	i = 0
	j = length
	while (j<=file_length):
		key = text[i:j] # Select a pattern of specifies length

		#check if we have the correct amount of characters
		if len(key)!= length: 
			break

		if key in pattern_count_dict:
			i+=1;j+=1
			continue

		pattern_count_dict.update({key:0})	

		# Now find the number of times the patter occured
		no_key_occurences = len(re.findall(key, text))
		pattern_count_dict[key] = no_key_occurences
		i+=1
		j+=1	

	return(pattern_count_dict)

def count_doubles(cipher_file):
	"""
	Counts the occurence of the double letters
	"""	

	double_letter_dict = {'AA':0, 'BB':0, 'CC':0, 'DD':0, 'EE':0,
	                      'FF':0, 'GG':0, 'HH':0, 'II':0, 'JJ':0,
	                      'KK':0, 'LL':0, 'MM':0, 'NN':0, 'OO':0,
	                      'PP':0, 'QQ':0, 'RR':0, 'SS':0, 'TT':0,
	                      'UU':0, 'VV':0, 'WW':0, 'XX':0, 'YY':0,
	                      'ZZ':0}

	text = cipher_file.readline()

	for key in double_letter_dict:
		no_key_occurences = len(re.findall(key, text))
		double_letter_dict[key] = no_key_occurences

	return(double_letter_dict)	


def main():
	
	input_file = open("plain.txt", "r")
	output_file = open("cipher.txt", "w")
	monolithic_subtitution(input_file, output_file)

	cipher_file = open("cipher.txt","r")
	cipher_alphabets_count = count_chars(cipher_file)
	print(cipher_alphabets_count)

	cipher_file = open("cipher.txt","r")
	digraphs_count = count_n_graphs(cipher_file,2)
	print(digraphs_count)

	cipher_file = open("cipher.txt","r")
	trigraphs_count = count_n_graphs(cipher_file,3)
	print(trigraphs_count)

	doubles_count = count_doubles(cipher_file)
	print(doubles_count)	


	            
if __name__ == '__main__':
	main()
