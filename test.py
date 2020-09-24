from application import getAnswers
import unittest


# input = "600 million dollars"
# x = 2

# print(getAnswers(input, x))

inputString ="$7,000"

#1. 'in' method: Returns a boolean - true or false

if '$' in inputString:
	print('Success')  # 'Success'

#2.  __contains__() method: Returns a boolean - true or false

if inputString.__contains__('$'):
    print('Success')  # 'Success'


#3.  .find() method: Returns the index of the searched string

if inputString.find('$') >= 0:
    print('Success')  # 'Success'
