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

	alphabets_count = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0,
	                  'f':0, 'g':0, 'h':0, 'i':0, 'j':0,
	                  'k':0, 'l':0, 'm':0, 'n':0, 'o':0,
	                  'p':0, 'q':0, 'r':0, 's':0, 't':0,
	                  'u':0, 'v':0, 'w':0, 'x':0, 'y':0,
	                  'z':0}

	while True:
		ch = cipher_file.read(1) #Reading file char by char
		if not ch:
			cipher_file.close()
			break
		try:
			ch = ch.lower()
			alphabets_count[ch] = alphabets_count[ch] + 1
		except:
			continue

	return(alphabets_count)		


def main():
	
	input_file = open("plain.txt","r")
	output_file = open("cipher.txt","w")
    monolithic_subtitution(input_file,output_file)
	
	cipher_file = open("cipher.txt","r")
	alphabets_count = count_chars(cipher_file)	             
	            
if __name__ == '__main__':
	main()
