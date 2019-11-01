import datetime as dt
import math
from itertools import count

#The function below is supposed to print out a message along with the time that
#the function was called. The function has an error though. You should call the
#function multiple times and see if you can spot the error. Why is the error occurring?
#def log_time(message, time=dt.datetime.now()):
 #   print("{0}: {1}".format(time.isoformat(), message))
  #  pass


#Complete the function below so that it prints the time correctly. If an argument
#is passed to the time parameter, the function should use the value of the argument
#If an argument is not passed to the time parameter, the function should generate
#the time, as shown in the function above.
def log_time(message, time= None):
    if time is None:
        time = dt.datetime.now()
    print("{0}: {1}".format(time.isoformat(), message))

#print ("{0}: {1}".format(dt.datetime.utcnow().isoformat(), ""))
log_time("", dt.datetime.utcnow())
log_time("", dt.datetime.now())
log_time("", dt.datetime.now())
log_time("")
log_time("")

#This function takes a list of ints as an argument, and returns a new list with the indices of the
#even numbers in `nums'. For example, if nums = [4, 3, 1, 0, 6], the function should return [0, 3, 4]. You
# should use the enumerate function. Can you do this with a list comprehension?
def indices_of_evens(nums):
    list = []
    count = 0
    for i in nums:
        if i % 2 == 0 :
            list.append(count)
        count+=1
    return list

nums = [4,3,1,0,6]
print(indices_of_evens(nums))

#Nums is a list of ints. Use the map and filter functions to return a new list that contains the square roots
#of all of the multiples of 6 in nums. See if you can do this in one line. Note: you'll need to import the sqrt
#function from the math package.
def square_roots_mult_6(nums):
    return filter(lambda x: (x ** 2) % 6 == 0,nums)

print(*square_roots_mult_6([4,3,1,0,6,36]))

#Nums is a list of ints. Use a list comphrehension to return a new list that contains the square roots
#of all of the multiples of 6 in nums. See if you can do this in one line.
def square_roots_mult_6_II(nums):
    return [x for x in nums if (x** 2 % 6 == 0)]

print(square_roots_mult_6_II([4,3,1,0,6,36]))

#'grades' is a dictionary where the keys are student names and the values are numeric grades.
#The function should return a new dictionary with the names and grades of all students whose grade
#is at least a 90.

#For example, if grades is,
#   {'al': 89,
#    'sue': 92,
#    ''joe': 90}

#Then the function should return
#   {
#    'sue': 92,
#    ''joe': 90}

#You should use a dictionary comphrehension
def greater_than_90(grades):
    return { key:val for key, val in grades.items() if (val >= 90)}

def otherGreater(grades):
    d={}
    for x in grades:
        d[x] = grades[x]
    for k,v in grades.items():
        if grades[k] < 90:
            del d[k]
    return  d

grade = {'al': 89,    'sue': 92,    'joe': 90}
print(greater_than_90(grade))


#'grades' is a dictionary where the keys are student names and the values are numeric grades.
#The function should print out the name and grade of each student, in descending order by grade.
#For example, if grades is the dictionary given above. The function should print,
# sue 92
# joe 90
# al 89

#Note that different students might have the same grade.

#NOTE: There is a python function named sorted that might be useful here.

def ordered_grades(grades):
    return sorted(grades.items(), key = lambda x : x[1], reverse = True)


grade = {'al': 89,    'sue': 92,    'joe': 90}
print(ordered_grades(grade))


#the function below creates a generator that generates the collatz numbers starting at n. Your code should use
#the yield keyword.
def collatz_generator(n):
    #collatz = set()
    yield n
    while n > 1:
        #collatz.add(n)
        if n % 2 == 1:
            n = 3 * n +1
            #collatz.add(n)
        else:
            n = n//2
            #collatz.add(n)
        yield n

print(*collatz_generator(25))
