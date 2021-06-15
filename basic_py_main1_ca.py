# here you find some Exercises for learning the basic python syntax including lists, loops and dicts

# Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum
def multiplication_or_sum(num1, num2):
  mult = num1 * num2 # calculate product of two number
  if mult > 1000: # check if product is less then 1000
    addition = num1 + num2  # product is greater than 1000 calculate sum
  else:
    addition = "smaller"
  return addition

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)


# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)

# Exercise 2: Given a range of the first 10 numbers, Iterate from the start number to the end number,
# and In each iteration print the sum of the current number and previous number
def sumNum(num):
# for-loop might be useful
  prev_num = 0 
  for i in range(0, num+1):
    print(i+prev_num)
    prev_num = i

print("Printing current and previous number sum in a given range(10)")
sumNum(10)

# Exercise 3: Given a string and an integer number n, remove characters from a string starting from zero up to n
# and return a new string
def removeChars(str,n):
  test = str
  output = test.replace(test[0:n], "")
  return output

string1 = "hello how do you do?"
string1[0:5]

print("The new string is:")
print(removeChars("transportmodelling",9))

# what do you have to change to get the first 7 characters?
def firstChars(str,n):
  test = str
  output = test[0:n]
  return output

print(firstChars("transportmodelling",7))


# Exercise 4: Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
sampleList = [34, 54, 67, 89, 11, 43, 94]

sampleList.append(sampleList[4])
sampleList[1] = sampleList[4]
sampleList.pop(5)

sampleList

# Exercise 5: Find out the index of 'age' of the given list
list1=['name', 'place of birth','age', 'town']

list1.index('age')
list1[2]

# Exercise 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
def find_divisible(numberList):
  for i in numberList:
    if i % 5 == 0:   
      print(i)

numList = [10, 20, 33, 46, 55]
find_divisible(numList)

# Exercise 7: Calculate income tax for the given income by adhering to the below rules
# first 10.000€ rate: 0%
# next 10.000€ rate: 10%
# remainung rate 20%
# test it with an income of 45.000€ (solution should be:6.000€)
income = 45000

def prog_tax(y):
  if y <= 10000:
    tax = 0
    return tax
  elif y <=20000:
    tax = (y - 10000) * 0.1
    return tax
  else:
    tax = (y-20000) * 0.2 + 10000 * 0.1
    return tax

print("Given income", income, "€")

print("Total tax to pay is", prog_tax(60000), "€")

# Exercise 8: Take and print every second element of the list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1,len(mylist), 2):
    print(mylist[i])

print(mylist)
len(mylist)

# Exercise 9: bring the list in the reverse order
mylist = [1, 2, 3, 4, 5, 6]
mylist.reverse()
print(mylist)

### option 2
mylist = [1, 2, 3, 4, 5, 6]
mylist[::-1]

#Exercise 10: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#hint: use the zip-function

### option 1
res = [i + j for i, j in zip(list1, list2)]
res

### option 2
another_list = []

for i, j in zip(list1, list2):
  another_list.append(i+j)

another_list

### option 3
list3 = []
len(list2)

for i in range(0,4):
  list3.append(list1[i] + list2[i])

list3


#Exercise 11: create a list from the given one that replaces all numbers that are not divisible by 5 with 'NaN'
list1 = [4, 5, 8, 16, 15, 20, 24, 25, 44, 50]

def nan_replace(lista):
  
  for i in range(0,len(lista)):
    if lista[i] % 5 == 0:   
      pass
    else:
      lista[i] = 'NaN'
  return lista

print(nan_replace(list1))

# Exercise 12: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict0 = dict(zip(keys, values))
dict0

### explanation
tuples = (('Ten', 10), ('Twenty', 20), ('Thirty', 30))
tuples = dict(tuples)
tuples['Twenty']
# Output should be: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# Exercise 13: Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

### option 1
dict3 = dict1
dict3.update(dict2)
dict3

### option 2
dict3 = {**dict1, **dict2}
dict3

# Exercise 14: Initialize dictionary with default values and access the individual data of 'Kelly'
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}



#Exercise 15: Delete set of keys ('name' & 'salary') from a dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# Exercise 16: Get the key & value of a minimum value from the following dictionary
dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# Exercise 17: Add a list of elements to a given set
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
# Note: Set is unordered.

# Exercise 18: Return a new set of identical items from a given two set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


# Exercise 19: Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


# Exercise 20: Check if two sets have any elements in common. If yes, display the common elements.
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}


# Exercise 21: Check if all items in the following tuple are the same
def check(sampleTuple):
