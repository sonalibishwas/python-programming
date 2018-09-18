from tempfile import mkstemp
from shutil import move
from os import fdopen,remove

temp_file,abs_path = mkstemp()
with fdopen(temp_file,"w") as new_file:
	with open("Brunch_02.txt","r") as old_file:
		for line in old_file:
			line = line.split("\n")[0]
			new_line = "021A"+line+".JPG\n"
			new_file.write(new_line)
#Remove original file
remove("Brunch_02.txt")
#Move new file
move(abs_path,"Brunch_02.txt")
