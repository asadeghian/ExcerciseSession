import os,glob

def find_file_names(path):
	return glob.glob(path+'/*/*.txt')

def main():
	print find_file_names('./cleaneddata')

main()
