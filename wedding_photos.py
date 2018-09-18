# input Foldername, subfoldername and a filename consisting list of photos
# output selected photos copied under this directory same structure
import os
import shutil

# read input arguments
import sys
Folder = sys.argv[1]
subfolder = sys.argv[2]
#Get original photos folder location
photo_location = "/Users/sonali/Downloads/MyWedding/"+Folder+"/"+subfolder
print "copying photos from location %s"%photo_location
select_photo = Folder+"_"+subfolder+".txt"
#fh = open(select_photo,"r")
#print fh.read()
final_location = "./ForAlbum/"+Folder+"/"+subfolder
print ("copying files to location = %s"%final_location) 
try:
	os.makedirs(final_location)
except:
	print "DIR exists"
with open(select_photo,"r") as fh:
	for line in fh:
		try:
			line = line.split("\n")[0]
			source = photo_location+"/"+line
			print "source = %s"%source
			shutil.copy(source,final_location)
			print "copied %s"%line
		except IOError as e:
			print "Error in file %s"%line
			print("Error:%s"%e)
