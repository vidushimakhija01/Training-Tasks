#Write a program to check if a number is prime or not
a = int(input('enter a number '))
if (a%2==0) :
    print('not prime')
else :
    print('is prime')

#Print all numbers from 1 to N that are divisible by both 3 and 5
n = int(input("enter a number "))
for i in range(1,n+1):
    if (i%3==0 and i%5==0):
        print(i)

#Find the sum of all even numbers from 1 to 100
sum = 0
for i in range(1,101):
    if (i%2==0):
        sum += i
print(sum)

#Check if a given year is a leap year using if-else
year = int(input('enter year '))
if (year%100!=0 and year%4==0):
    print('leap year')
elif (year%400==0):
    print('leap year')
else:
    print('normal year')

#Print the factorial of a number using a loop
n = int(input("enter a number "))
factorial = 1
for i in range (1,n+1):
    factorial *= i
print(factorial)

#Write a program to count the number of words in a string using a loop
str = input('enter a string ')
words = 1
for i in str.strip():
    if (i == ' '):
        words += 1
print('number of words in string are', words)

#Find the largest of three numbers using if-else
a = int(input('a:enter a number '))
b = int(input('b:enter a number '))
c = int(input('c:enter a number '))
if (a>b and a>c):
    print(a)
elif (b>a and b>c):
    print(b)
else :
    print('largest number is three:',c)

#Given a number 1-7, print the day of the week using switch-case
num = int(input('enter day number '))
match num:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
        
#Write a program to reverse a number using a loop
num = int(input("Enter a number: "))
reverse = 0
while (num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)

#Check whether a character is a vowel or consonant using switch-case
char = input('enter a letter ')
match char.lower():
    case 'a':
        print('Vowel')
    case 'e':
        print('Vowel')
    case 'i':
        print('Vowel')
    case 'o':
        print('Vowel')
    case 'u':
        print('Vowel')
    case _:
        print('Consonant')
        
#Print the multiplication table of a number using a loop
num = int(input('enter a number '))
print('multiplication table of', num, ':')
for i in range(1,11):
    print(num,'*',i,'=',num*1)

#Check if a number is positive, negative, or zero using if-else
num = int(input('enter a number '))
if (num>0):
    print('positive')
elif (num<0):
    print('negative')
else:
    print('zero')

#Write a program to calculate the average of numbers in an array using a loop
arr = [1,2,3,4,5]
avg =0
for i in arr:
    avg += i
avg /= len(arr)
print(avg)

#Print Fibonacci series up to N terms using a loop
num = int(input('enter a number '))
a, b = 0,1
print('Fibonacci Series:')
for i in range(num):
    print(a, end=' ')
    a,b = b, a+b

'''
Write a program to take a character input 
and print whether it is an alphabet, digit, or special character using if-else
'''
char = input('enter a character ')
if(char.isalpha()):
    print('alphabet')
elif(char.isdigit()):
    print('digit')
else:
    print('special character')

#Given a month number, print the season (e.g., summer, winter) using switch-case
num = int(input('enter month number '))
match num:
    case 1|2|11|12:
        print('Winter')
    case 3|4:
        print('Spring')
    case 5|6|7:
        print('Summer')
    case 8|9:
        print('Monsoon')
    case 10:
        print('Autumn')
    case _:
        print('Invalid Month Number')

#Count the number of vowels in a given string using a loop and if-else
str = input('enter a string ')
vowels = 0
for i in str.strip():
    if i.lower() in 'aeiou':
        vowels += 1
print('number of vowels in string are', vowels)

#Write a simple calculator using switch-case for operations (+, -,*, /)
num1 = int(input('enter first number '))
num2 = int(input('enter second number '))
operator = input('enter the operator(+,-,*,/) ')
match operator:
    case '+':
        print(num1,operator,num2,'=',num1+num2)
    case '-':
        print(num1,operator,num2,'=',num1-num2)
    case '*':
        print(num1,operator,num2,'=',num1*num2)
    case '/':
        print(num1,operator,num2,'=',num1/num2)

#Print all elements in a list/array greater than a given value using a loop and if-else
arr = [1,2,3,4,5]
num = int(input('enter number '))
for i in arr:
    if i>num:
        print(i)

#Check if a given string is a palindrome using a loop and if-else
str = input('enter a string ')
is_palindrome = True
for i in range(len(str)//2):
    if(str[i]!=str[-(i+1)]):
        is_palindrome = False
        break
if is_palindrome:
    print('palindrome')
else:
    print('not a palindrome')