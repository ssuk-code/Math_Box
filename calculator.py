# 기본 계산기
def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide_new(a, b):
	return a / b

def getMedian(a, b):
    return (a + b) / 2

def getRemainder(a, b):
	return a // b﻿

def get_Abs(num):
	if num >= 0:
		return num
	else:
		return -num

def getPercent(a, b):
    return (a / b) * 100

def get_Sum_ver2(n):
	sum = 0
	for i in range(1, n+1):
		sum = sum + i

	return sum
