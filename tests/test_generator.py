import unittest
import json
import sys
from dictdiffer import diff, patch, swap, revert
from generator.file_and_diff_generator import file_generator1, diff_generator


class DiffFileTestCase(unittest.TestCase):
	def test_same_file_check(self):
		json_list = file_generator1(['second act', 'deadpool', 'aquaman', 'bumblebee'], 5, 'file1.txt')
		#print(json_list)
		json.dump(json_list, open('file1.txt', 'w'))
		diff_file = diff_generator('file1.txt', 'file1.txt') #checking if there is a difference if the same files are compared
		assert len(list(diff_file)) == 0		
	

if __name__  == '__main__':
	unittest.main()
