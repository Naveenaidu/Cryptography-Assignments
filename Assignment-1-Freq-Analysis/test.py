def monolithic_subtitution(input_file,output_file):
	"""
	Substitutes plain text letters with cipher text letters.
	Replaces each plain text letter with it's monolithic 
	substitution and writes it to the outputfile. 

	Ignores whitespace and all the special characters

	param
		
		input_file : The plaintext file 
		output_file: The file with the monolithic substitution

	alphabets: List of dictionary where {'key':'value'} refers to
	           {'letter':'substitution-letter'}
	"""

	alphabets = {'a':'D', 'b':'E', 'c':'F', 'd':'G', 'e':'H',
	             'f':'I', 'g':'K', 'h':'J', 'i':'L', 'j':'M',
	             'k':'R', 'l':'Q', 'm':'P', 'n':'O', 'o':'N',
	             'p':'S', 'q':'T', 'r':'U', 's':'V', 't':'W',
	             'u':'X', 'v':'Y', 'w':'Z', 'x':'B', 'y':'A',
	             'z':'C'}

	while True:
		ch = input_file.read(1)
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


def main():
	
	input_file = open("plain.txt","r")
	output_file = open("cipher.txt","w")

	monolithic_subtitution(input_file,output_file)	             
	            
if __name__ == '__main__':
	main()
