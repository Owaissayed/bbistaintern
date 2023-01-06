# def simple_interest(p, t, r):
#     print('The principal is', p)
#     print('The time period is', t)
#     print('The rate of interest is', r)
#
#     si = (p * t * r) / 100
#
#     print('The Simple Interest is', si)
#     return si
# simple_interest(8, 6, 8)
#
#
# #Find compound interest for given values.
#
#
# def compound_interest(principal, rate, time):
# 	Amount = principal * (pow((1 + rate / 100), time))
# 	CI = Amount - principal
# 	print("Compound interest is", CI)
#
# compound_interest(10000, 10.25, 5)
#
# Python program to determine whether
# the number is Armstrong number or not
#
# Function to calculate x raised to
# the power y
# def power(x, y):
#     if y == 0:
#         return 1
#     if y % 2 == 0:
#         return power(x, y // 2) * power(x, y // 2)
#
#     return x * power(x, y // 2) * power(x, y // 2)
#
#
# # Function to calculate order of the number
# def order(x):
#     # Variable to store of the number
#     n = 0
#     while (x != 0):
#         n = n + 1
#         x = x // 10
#
#     return n
#
#
# # Function to check whether the given
# # number is Armstrong number or not
# def isArmstrong(x):
#     n = order(x)
#     temp = x
#     sum1 = 0
#
#     while (temp != 0):
#         r = temp % 10
#         sum1 = sum1 + power(r, n)
#         temp = temp // 10
#
#     # If condition satisfies
#     return (sum1 == x)
#
#
# # Driver code
# x = 153
#
# print(isArmstrong(x))
#
# x = 1253
# print(isArmstrong(x))
#
# Python program to find Area of a circle
#
# def findArea(r):
# 	PI = 3.142
# 	return PI * (r*r);
#
# # Driver method
# print("Area is %.6f" % findArea(765));
#
#
# BMI calculator
# height=float(input('Your height in meters? '))
# weihgt=float(input('Your weight in kilograms? '))
# bmi=weihgt/height**2
# print(bmi)
#
#
# weeks in life
#
# age = input("What is your current age? ")
#
# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)
#
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
#
#
# tip calculator
# print('Welcome to tip calculator!')
#
# totalbill = float(input('What was the total amount of bill? '))
#
# tip = int(input('What percent of tip would like to give? '))
# finalbill=totalbill+((totalbill*tip)/100)
# people = int(input('How many people to split the bill? '))
# split=round((finalbill/people),2)
# print(f'Each person should pay {split}')
#
# odd and even number
# number=int(input('Enter a number: '))
# if number%2==0:
#     print('It is a even number.')
# else:
#     print("It is a odd number.")
#
# bmi2.0 calculator
# height=float(input('Enter your height in meters: '))
# weight=int(input('Enter your weight in kilograms: '))
#
# bmi=round(weight/height**2)
# if bmi<18.5:
#     print(f'Your bmi is {bmi}. You are underweight.')
# elif bmi<25:
#     print(f"Your bmi is {bmi}. You have a normal weight.")
# elif bmi<30:
#     print(f'Your bmi is {bmi}. You are slightly obese.')
# elif bmi<35:
#     print(f'Your bmi is {bmi}. You are obese.')
# else:
#     print(f'Your bmi is {bmi}. You are clinically obese.')
#
# leap year
# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print(" Leap year.")
# else:
#   print("Not leap year.")
#
# rollercoaster ride
# print('Welcome! To rollercoaster.')
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#
#
# pizza order
#
#
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
#
#
# bill = 0
# if size == "S":
#    bill += 15
# elif size == "M":
#    bill += 20
# elif size == "L":
#    bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is $ {bill} ")
#
#
#
#
# love calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# bothname = name1 + name2
# lowername = bothname.lower()
# t = lowername.count("t")
# r = lowername.count("r")
# u = lowername.count("u")
# e = lowername.count("e")
# digit1 = t + r + u + e
#
# l = lowername.count("l")
# o = lowername.count("o")
# v = lowername.count("v")
# e = lowername.count("e")
# digit2 = l + o + v + e
# score = int(str(digit1) + str(digit2))
# if (score<10) or (score>90) :
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif score>=40 and score<=50:
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
#
# heads tails
# import random
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# number=random.randint(0,1)
# if number==1:
#   print("Heads")
# else:
#   print('Tails')
#
# banker roulette
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x=len(names)
X=x-1

selected_num=random.randint(0,X)

selected_name=names[selected_num]

print(f"{selected_name} is going to buy the meal today!")