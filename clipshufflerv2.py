import os
import sys
import os.path
import random 
# import getopt
# from random import shuffle
######################################################################	
######################################################################	OK
def main():

	print("Clip Shuffler V.2\n")
	MAXFILE = 30
	playlistpath = "H:\BORDELATRIER\listshuffle.asx"
	clippath = 'H:\BORDELATRIER\ClipAGouter'

	cliplisted = listdirectory(clippath)
	clipshuffler(cliplisted, MAXFILE,playlistpath)
	print('\nenjoy!')
######################################################################	
######################################################################
def listdirectory(path):
	print("\tListdirectory")  
	allclip ={}
	nbfile=0 
	for root, dirs, files in os.walk(path):  
		for i in files:
			if i.endswith(".mp4") or i.endswith(".avi") or i.endswith(".mkv") or i.endswith(".mpg") or i.endswith(".mpeg"):
				nbfile=nbfile+1
				allclip[i]=os.path.join(root, i)

	return allclip

######################################################################	
######################################################################	
def clipshuffler(listc,nb,asxfilepath):
	print("\tShuffle")
	items=listc.items()
	ritems=random.shuffle(items)
	oftmp=open(asxfilepath,"w")
	oftmp.write('<ASX Version = "3.0" >\n\n')
	for key, value in items:
		# print key, value
		oftmp.write('\t<Entry>\n\n\t\t<Title>')
		oftmp.write(key)
		oftmp.write('</Title>\n\n\t\t<Ref href = "')
		oftmp.write(value)
		oftmp.write('" />\n\n\t</Entry>\n\n')	
	oftmp.write('</ASX>')
	oftmp.close()
	
######################################################################	
######################################################################	
if __name__ == '__main__':
	main()
