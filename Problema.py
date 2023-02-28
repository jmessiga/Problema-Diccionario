import time
import random

#Generates a list of n random numbers, ranging from 0 to 10^9
#Input: n, an integer number
#Output: lis, a list of random integer numbers
def list_generation(n):
    lis=[]
    for i in range(0,n-1):
        num=random.randint(0,10**9)
        lis.append(num)
    return lis

#Calculates the time in a certain instant
#Input: N/A
#Output: time 
def timing():
    t=time.time()
    return t

#Calculates the time lapse between to calls of the function "timing"
#Inputs: begin and ending, two times at which the "timing" function was called
#Output: Time lapse within those two calls
def time_lapse(begin,ending):
    lapse=ending-begin
    return lapse

#Determines if one of the elements of the list "Lis" doubles other element of it. Uses a dictionary. 
#Inputs: the list "lis"
#Output: Returns True if one of the elements doubles other element. Else, returns False.
def some_other_function (lis):
    dic={}
    
    i=0
    for elem in lis:
        dic.update({(elem):i})
        i+=1
    #print(dic)
    
    for cmp in lis:
        doub=2*cmp
        
        if dic.get(doub):
            #print(cmp)
            return True
    
    return False

#Determines if one of the elements of the list "Lis" doubles other element of it. Uses a list. 
#Inputs: the list "lis"
#Output: Returns True if one of the elements doubles other element. Else, returns False.
def some_function (lis):
    
    for i in range(len(lis)):
        for j in range(len(lis)):
            if 2*lis[j]==lis[i]:
                return True
    
    return False

#Defines the number of elements in the list
Numbers=10**6

#List generation using the function "list_generation"
Lis=list_generation(Numbers)

#First call of function "timing" 
Begin=timing()

#some_function call
Val=some_function (Lis)

#Second call of function "timing" 
Ending=timing()

#Time lapse calculation. Calculates the time lapse due to using "some_function".
Lapse=time_lapse(Begin,Ending)
print("some_function CPU time: %11.10f" %Lapse)

#First call of function "timing" 
Begin2=timing()

#some_other_function call
Val2=some_other_function (Lis)

#Second call of function "timing" 
Ending2=timing()

#Time lapse calculation. Calculates the time lapse due to using "some_other_function".
Lapse2=time_lapse(Begin2,Ending2)
print("some_other_function CPU time: %11.10f" %Lapse2)
