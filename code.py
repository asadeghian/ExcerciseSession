import os,glob

def find_bad_gender(file_line):
	if file_line.find(': N') == -1:
		return 0
	return 1

def find_file_names(path):
	return glob.glob(path+'/*/*.txt')

def main():
	for i in find_file_names('./cleaneddata'):
		f=open(i)
		for line in f:
			if find_bad_gender(line) == 1:


main()
