#print(2)
#print (2019 - 2000)
#print(-2*100)

#print("hey jude", "don't make it bad") #quotes go in pairs to differentiate
#print('hey jude') #single quotes ok for single string
#print('hey jude', 'do not make it bad') #no apostrophe - ok to have single quote

#print ("1+2+3=", 1+2+3)

#name = input() #function to input value
#print('hello', name)

#n=100
#print(n) #prints value above

#a='ABC'
#b=a
#a="XYZ"
#print('a is', a,'. b is', b)

first_name="val"
last_name="tetu"
name=first_name+" "+last_name

#print(first_name+" "+last_name)
#print(first_name*20)
#print('hello, {}! you are {} years old.'.format(name, 20)) #inputs the name and 20 into curly brackets

#template='hello, {}! you are {} years old.'
#name1='dan'
#age1 = 20
#name2='anna'
#age2 = 18
#print(template.format(name1, age1))
#print(template.format(name2, age2))

#print('pi equals {:.2f}'.format(3.14159)) #formatted - f is floating number, column: format differently, .2:keep 2 decimal places

#template='Hello, {name}! You are {age} years old'
#print(template.format(age=age1, name=name1))

#import math #imports package of functions
#print(math.pow(2,5)) #put in 2 arguments in function, 2^5
#print(math.pi)

#print(2**2) #2^2

#03/16
#exercise 2.1
#NUM_SEC_ONE_MIN=60
#seconds=42*NUM_SEC_ONE_MIN+42
#print(seconds)
##exercise 2.2
#NUM_KM_ONE_MILE=1.61
#miles=10/NUM_KM_ONE_MILE
#print(miles)

#Exercise 1.1 Chap 1
#r=input("please enter number:")
#r=int(r) #converts to integer
#volume = (4/3)*math.pi*math.pow(r,3)
#print('the volume is of a phere of {} is {:.3f}.'.format(r,volume))

#1.3
#hour=3
#minutes=2
#print("current time is {:02}:{:02}.".format(hour,minutes))
#print(1+2)
#import datetime
#now=datetime.datetime.now()
#print(now)
#print(now.hour, now.minute,now.second)

#print(3.14e-2) #prints floating number

#length_num=len(str(2**1000000)) #how long string is
#print(length_num)
#print(len('Valerie'))

#import math
#print(math.pi)
#print(math.sqrt(25))

#import random
#print(int(random.random()*100)) #random int between 0 and 100, gives REAL number (not int)
#print(random.randint(1,6)) #random int between 1 and 6
#print(random.choice([1,2,3,4,5,6])) #chooses value (can be int, floating, string, etc.) between brackets
#print(random.choice(['val', 'dan', 'Flower']))

#Strings
#I'm "OK"
#print("I'm \"OK\".") #\differentiates quote mark
#print('I\'m learning\nPython.') #second backslash tells python to start in new line
#print('I love \n\nthe sun.') #two spaces

#Boolean
#print(3>2) #returns true
#print(3>2 and 3>5) #and connects 2 expressions together
#print(3>2 or 3>5) #if one is true, then returns true
#print(3>2 or 3>5 or False or 100>100)
#n=int(input()) #have to input value for n
#print(n>3)

age=int(input("how old are you?"))
is_in_us = True
answer = input('are you in the US?')
if answer == 'no'
    is_in_us = False
if age>=21:
    print('yes you can.')
else:
    print('sorry you cannot.')



