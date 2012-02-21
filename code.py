import os,glob,string 
from shutil import move

def file_fixer(file_name,line):
	from tempfile import mkstemp
	fh, abs_path = mkstemp()

	o=open(file_name)
	new_file = open(abs_path,'w')

	for line2 in o:
		print line,line2
		if line==line2:
			line2= line2.replace(": N",": M")
		new_file.write(line2)
   	new_file.close()
    	o.close()
    	#Remove original file
    	os.remove(file_name)
    	#Move new file
    	move(abs_path, file_name)



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
				file_fixer(i,line)


main()
