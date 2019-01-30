"""
Author: Spencer Fleming
File Name: stat_functions.py
Description: collection of functions that take in a list of floats and compute some statistic
"""
import math

def sum(nums):
	s = 0.0
	for l in nums:
		s += l
	return s

def mean(nums):
	return sum(nums)/float(len(nums))

def standard_deviation(nums):
	temp_sq = list()
	for l in nums:
		temp_sq.append(l**2)
	temp_m = (sum(nums)**2)/float(len(nums))
	ret = (sum(temp_sq) - temp_m)/float(len(nums)-1)
	return math.sqrt(ret)

def coefficient_of_variation(nums):
	return (standard_deviation(nums)/mean(nums)) * 100.0

def median(nums):
	temp = nums[:]
	while(len(temp) >= 3):
		temp.pop()
		temp.pop(0)
	if(len(temp) == 1):
		return temp[0]
	if(len(temp) == 2):
		return (temp[0] + temp[1])/2.0

def min(nums):
	return nums[0]

def max(nums):
	return nums[len(nums)-1]

def quartile_one(nums):
	temp = nums[:]
	return median(temp[:int(len(temp)/2)])

def quartile_three(nums):
	temp = nums[:]
	if (len(temp)%2 == 0):
		return median(temp[(int(len(temp)/2)):])
	return median(temp[(int(len(temp)/2))+1:])

def interquartile_range(nums):
	return quartile_three(nums) - quartile_one(nums)

	


