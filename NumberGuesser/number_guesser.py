#importing libraries required
import random as rm
import numpy as np

#getting random number
rand = rm.randrange(0, 100, 1)

#getting user input
print("Enter a random number between 0 and 100")
user_input = int(input())
#to keep track of number of tries
count = 0

while rand != user_input and count < 10:
    #hints
    if(rand > user_input):
        #to calculate difference between random number and user input
        diff =  rand - user_input
        if(diff >= 50):
            print("Go much higher")
            user_input = int(input())
            count = count + 1
        elif(diff >= 25 and diff < 50):
            print("Go higher")
            user_input = int(input())
            count = count + 1
        elif(diff > 0 and diff < 25):
            print("Go slightly higher")
            user_input = int(input())
            count = count + 1
    elif(rand < user_input):
        #to calculate difference between random number and user input
        diff = user_input - rand
        if(diff >= 50):
            print("Go much lower")
            user_input = int(input())
            count = count + 1
        elif(diff >= 25 and diff < 50):
            print("Go lower")
            user_input = int(input())
            count = count + 1
        elif(diff > 0 and diff < 25):
            print("Go slightly lower")
            user_input = int(input())
            count = count + 1

print("Success")
print("No of tries: ", count)