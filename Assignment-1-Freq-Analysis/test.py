import re
from operator import itemgetter

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

def count_occurences(text,length):
	"""
	Count the number of digraphs and trigraphs and single letters

	params:
		cipher_file: file with the cipher text
		length: The length of the string pattern

	pattern_count_dict: Dictionary which holds the pattern and
						the count of it's occurence in the file.						

	This function reads the file and starts making pairs/ 
	triplets string pattern from the first character.	   
	"""
	pattern_count_dict = {}

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

		# Fzind the number of times the patter occured
		no_key_occurences = len(re.findall(key, text))
		pattern_count_dict[key] = no_key_occurences
		i+=1
		j+=1	

	return(pattern_count_dict)

def count_doubles(text):
	"""
	Counts the occurence of the double letters
	"""	

	double_letter_dict = {'AA':0, 'BB':0, 'CC':0, 'DD':0, 'EE':0,
	                      'FF':0, 'GG':0, 'HH':0, 'II':0, 'JJ':0,
	                      'KK':0, 'LL':0, 'MM':0, 'NN':0, 'OO':0,
	                      'PP':0, 'QQ':0, 'RR':0, 'SS':0, 'TT':0,
	                      'UU':0, 'VV':0, 'WW':0, 'XX':0, 'YY':0,
	                      'ZZ':0}

	for key in double_letter_dict:
		no_key_occurences = len(re.findall(key, text))
		double_letter_dict[key] = no_key_occurences

	return(double_letter_dict)

def calculate_frequency(text,dictionary,num_char_in_key):
	"""
	Finds the frequency of each character.

	num_char_key: The value can be either 1,2,3. 
				  1 --> Single charcter
				  2 --> Digraphs/Doubles
				  3 --> Trigraphs
	"""
	text_len = len(text)
	total_number = int(text_len/num_char_in_key)
	freq_dict = dictionary

	for key in freq_dict:
		frequency = (freq_dict[key]/total_number)*100
		freq_dict[key] = round(frequency,2) 

	return freq_dict

def print_cipher_alphabets(alphabets_dict):
	sorted_list = sorted(alphabets_dict.items(),
		          key = itemgetter(1),reverse=True)

	dash = "-"
	space = " "

	print('*'*70)	
	print( dash*12 + " Frequency of the letters in Cipher Text are "
		   + dash*12)
	print("LETTER" + space*5 + "Frequency")
	for key,value in sorted_list:
		print(space*3 + str(key) + space*10 
			  + str(alphabets_dict[key]))
	print('*'*70+'\n')

def print_digraphs(digraphs_dict):
	sorted_list = sorted(digraphs_dict.items(),
		          key = itemgetter(1),reverse=True)

	dash = "-"
	space = " "
	print("The most common digraphs in English languages is: \n")
	print("   TH,HE,AN,IN,ER,ON,RE,ED,ND,HA,AT,EN \n")
	print("The most common digraphs in the message are: \n")
	print(dash*12 + " Frequency of Digraphs " + dash*12)
	print("Pattern" + space*5 + "Frequency")

	for key,value in sorted_list[:10]:
		print(space*3 + str(key) + space*10 
			  + str(digraphs_dict[key]))
	print('*'*70+'\n')

def print_doubles(doubles_dict):
	sorted_list = sorted(doubles_dict.items(),
		          key = itemgetter(1),reverse=True)

	dash = "-"
	space = " "
	print("The most common doubles in English languages is: \n")
	print("    SS,EE,TT,FF,LL,MM,OO \n")
	print("The most common doubles in the message are: \n")
	print(dash*12 + " Frequency of Doubles " + dash*12)
	print("Pattern" + space*5 + "Frequency")

	if sorted_list[0][1]:
		for key,value in sorted_list[:10]:
			print(space*3 + str(key) + space*10 
				  + str(doubles_dict[key]))
	else:
		print("There are no double letters in the cipher text")		
	print('*'*70+'\n')

	
def print_trigraphs(trigraphs_dict):
	sorted_list = sorted(trigraphs_dict.items(),
		          key = itemgetter(1),reverse=True)

	dash = "-"
	space = " "
	print("The most common trigraphs in English languages is: \n")
	print("    THE,AND,THA,ENT,ION,TIO,FOR,NDE,HAS,NCE,TIS,OFT,MEN \n")
	print("The most common trigraphs in the message are: \n")
	print(dash*12 + " Frequency of Trigraphs " + dash*12)
	print("Pattern" + space*5 + "Frequency")

	for key,value in sorted_list[:12]:
		print(space*3 + str(key) + space*10 
			  + str(trigraphs_dict[key]))
	print('*'*70+'\n')
          		
def substitution(dictionary,cipher_file,decrypt_file):
	"""
	Subsitutes the cipher text with the most occuring letters
	of the english language. 
	"""
	ordered_list = sorted(dictionary.items(),
		          key = itemgetter(1),reverse=True)

	list1 = ['e','t','o','n','i','s','a','h','r','d','l',
	         'c','u','m','f','w','g','y','p','b','v','k',
	         'j','x','q','z']
	dictionary1 = {}

	for x in ordered_list:
		dictionary1.update({x[0]:' '})

	i = 0;
	
	for key in dictionary1:
		dictionary1[key] = list1[i]
		i+=1

	print(dictionary1)
	while True:
		ch = cipher_file.read(1) #Reading file char by char
		if not ch:
			break
		decrypt_file.write(dictionary1[ch].lower())				


def main():
	
	input_file = open("plain.txt", "r")
	output_file = open("cipher.txt", "w")
	monolithic_subtitution(input_file, output_file)

	cipher_file = open("cipher.txt","r")
	cipher_file_content = cipher_file.readline()

	# Dictionary of occurences

	cipher_alphabets_dict = count_occurences(cipher_file_content,1)
	digraphs_dict = count_occurences(cipher_file_content,2)
	trigraphs_dict = count_occurences(cipher_file_content,3)
	doubles_dict = count_doubles(cipher_file_content)

	# Calculate the frequency

	alphabets_freq =  calculate_frequency(cipher_file_content,
		              cipher_alphabets_dict,1)
	digraphs_freq  =  calculate_frequency(cipher_file_content,
		              digraphs_dict,2)
	doubles_freq   =  calculate_frequency(cipher_file_content,
		              doubles_dict,2)
	trigraphs_freq =  calculate_frequency(cipher_file_content,
		              trigraphs_dict,3)

	# Printing the frequencies

	print_cipher_alphabets(alphabets_freq)
	print_digraphs(digraphs_freq)
	print_doubles(doubles_freq)
	print_trigraphs(trigraphs_freq)

	# Decrytpted text
	decrypt_file = open("decrypt.txt","w")
	cipher_file = open("cipher.txt","r")
	substitution(alphabets_freq,cipher_file,decrypt_file)

	            
if __name__ == '__main__':
	main()
