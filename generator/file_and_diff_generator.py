import requests
import json
import shutil
import random
from dictdiffer import diff, patch, swap, revert
import ast

def main():
	movies=['second act','deadpool','aquaman','bumblebee']
	file_generator1(movies,10,'fileT.txt') #generates the first large dataset file
	file_generator2(movies,10,'fileV.txt') #generates the second large dataset file
	diff_generator('fileT.txt','fileV.txt') #generates the difference between the two dataset files
	

def file_generator1(movies_list,count,filename): #this module generates the first file
	file_handle1=open(filename,'w') #open first file in write mode
	counter=1
	json_list=[] #make a list of jsons
	while(counter<=count):
		movie=movies_list[counter%4]
		movie=movie.replace(' ','+')
		url='http://www.omdbapi.com/?i=tt3896198&apikey=bb039509&t='+movie #make a url with a list of movies above
		counter=counter+1
		response=requests.get(url)
		json_value=response.json()
		json_list.append(json_value) #add the response to the URL into a list
	json.dump(json_list,file_handle1)
	file_handle1.close()
	return json_list
	
	

def file_generator2(movies_list,count,filename): #this module generates the second file
	file_handle2=open(filename,'w') #open third file in write mode , made to differ with the first file
	counter=1
	json_list=[] #make a list of jsons
	while(counter<=count):
		movie_index=random.randint(0,3)
		movie=movies_list[movie_index]
		movie=movie.replace(' ','+')
		url='http://www.omdbapi.com/?i=tt3896198&apikey=bb039509&t='+movie #make a url with a list of movies above
		counter=counter+1
		response=requests.get(url)
		json_value=response.json()
		json_list.append(json_value) #add the response to the URL into a list
	json.dump(json_list,file_handle2)
	file_handle2.close()
	return json_list
	

def diff_generator(filename1,filename2): #this module calculates the difference between the files

	# pip install dictdiffer
	file_diff = diff(json.load(open(filename1,'r')), json.load(open(filename2,'r')))
	file_handle4=open('output.txt','w')
	
	for a in file_diff:
		file_handle4.write(str(a))  #output.txt will contain the diff of both the files
	file_handle4.close()
	return file_diff
		


if __name__ == '__main__':
    main()
	