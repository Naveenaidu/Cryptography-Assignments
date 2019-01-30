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
		try:
			alphabets_count[ch]+= 1
		except:
			continue

	return(alphabets_count)

def count_digraphs(cipher_file):
	return	


def main():
	
	input_file = open("plain.txt", "r")
	output_file = open("cipher.txt", "w")
	monolithic_subtitution(input_file, output_file)

	cipher_file = open("cipher.txt","r")
	cipher_alphabets_count = count_chars(cipher_file)
	print(cipher_alphabets_count)	             
	            
if __name__ == '__main__':
	main()
