# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:31:01 2020

@author: mcsbi
"""
"""
Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].
"""
def squares(start, end):
	square=[]
	for numbers in range(start,end+1):
		n_square = numbers*numbers
		square.append(n_square)
	return square

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
