from difflib import SequenceMatcher 

with open('Testfile1.txt') as first_file, open('Testfile2.txt') as second_file: 
	
	file1 = first_file.read() 
	file2 = second_file.read() 
	
	ab = SequenceMatcher(None, file1, 
						file2).ratio() 
	
	result = int(ab*100) 
	print(f"{result}% Plagiarized Content") 
