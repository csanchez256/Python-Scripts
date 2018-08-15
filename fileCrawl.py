# Run this python program in the terminal. Change the rootDir to 
# the folder that you want to start traversing
# Chris Sanchez 8/15/18

import os, shutil
import glob

# define the directory you want to crawl
rootDir = 'C:/Users/PC 1/Documents/Programs/TEST'


def removeFiles():
	# for all folders, subfolders etc... walk through
	for dirName, subdirList, fileList in os.walk(rootDir):
		print('Found directory: %s' % dirName)

    	# If the file ends in .wmv, then delete it
		for file_name in fileList:
			print('\t%s' % file_name)
			if (file_name.endswith(".wmv")):
				os.remove(os.path.join(dirName, file_name))


removeFiles()