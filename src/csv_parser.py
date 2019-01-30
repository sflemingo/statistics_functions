"""
Author: Spencer Fleming
File Name: csv_parser.py
Description: parses a csv file and gives statistics on the data
"""
import stat_functions
import sys

def display_stats(nums):
	print('sum: ' + str(round(stat_functions.sum(nums),3)))
	print('mean: ' + str(stat_functions.mean(nums)))
	print('standard deviation: ' + str(stat_functions.standard_deviation(nums)))
	print('coefficient of variation: ' + str(stat_functions.coefficient_of_variation(nums)))
	print('min: ' + str(stat_functions.min(nums)))
	print('max: ' + str(stat_functions.max(nums)))
	print('quartile one: ' + str(stat_functions.quartile_one(nums)))
	print ('median: ' + str(stat_functions.median(nums)))
	print ('quartile three: ' + str(stat_functions.quartile_three(nums)))
	print('interquartile range: ' + str(stat_functions.interquartile_range(nums)))

def main():
	if len(sys.argv) > 1:
		fname = sys.argv[1]
		f = open("data/" + fname, "r")
		nums = list()
		for line in f.readlines():
			for num in line.strip('\n').split(','):
				nums.append(float(num))
		nums.sort()
		display_stats(nums)

if __name__ == '__main__':
    main()
