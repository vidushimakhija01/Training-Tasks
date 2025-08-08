import datetime
functions = {
    '1' : 'Write a program to check if a number is prime or not',
    '2' : 'Print all numbers from 1 to N that are divisible by both 3 and 5',
    '3' : 'Find the sum of all even numbers from 1 to 100',
    '4' : 'Check if a given year is a leap year using if-else',
    '5' : 'Print the factorial of a number using a loop',
    '6' : 'Write a program to count the number of words in a string using a loop',
    '7' : 'Find the largest of three numbers using if-else',
    '8' : 'Given a number 1-7, print the day of the week using switch-case',
    '9' : 'Write a program to reverse a number using a loop',
    '10' : 'Check whether a character is a vowel or consonant using switch-case',
    '11' : 'Print the multiplication table of a number using a loop',
    '12' : 'Check if a number is positive, negative, or zero using if-else',
    '13' : 'Write a program to calculate the average of numbers in an array using a loop',
    '14' : 'Print Fibonacci series up to N terms using a loop',
    '15' : 'Write a program to take a character input and print whether it is an alphabet, digit, or special character using if-else',
    '16' : 'Given a month number, print the season (e.g., summer, winter) using switch-case',
    '17' : 'Count the number of vowels in a given string using a loop and if-else',
    '18' : 'Write a simple calculator using switch-case for operations (+, -,*, /)',
    '19' : 'Print all elements in a list/array greater than a given value using a loop and if-else',
    '20' : 'Check if a given string is a palindrome using a loop and if-else',
}
for key, value in functions.items():
    print(f"{key}: {value}")
x = int(input('hello, which function would you like to perform'))

def isprime():
    a = int(input('enter a number '))
    if (a%2==0) :
        print('not prime')
    else :
        print('is prime')

def divisible():
    n = int(input("enter a number "))
    for i in range(1,n+1):
        if (i%3==0 and i%5==0):
            print(i)

def sum_even():
    sum = 0
    for i in range(1,101):
        if (i%2==0):
            sum += i
    print(sum)

def leap_year():
    year = int(input('enter year '))
    if (year%100!=0 and year%4==0):
        print('leap year')
    elif (year%400==0):
        print('leap year')
    else:
        print('normal year')

def factorial():
    n = int(input("enter a number "))
    factorial = 1
    for i in range (1,n+1):
        factorial *= i
    print(factorial)

def no_of_words():
    str = input('enter a string ')
    words = 1
    for i in str.strip():
        if (i == ' '):
            words += 1
    print('number of words in string are', words)

def largest():
    a = int(input('a:enter a number '))
    b = int(input('b:enter a number '))
    c = int(input('c:enter a number '))
    if (a>b and a>c):
        print(a)
    elif (b>a and b>c):
        print(b)
    else :
        print('largest number is three:',c)

def day_of_week():
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

def number_reverse():
    num = int(input("Enter a number: "))
    reverse = 0
    while (num > 0):
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    print("Reversed number:", reverse)

def check_letter():
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

def multiplication_table():
    num = int(input('enter a number '))
    print('multiplication table of', num, ':')
    for i in range(1,11):
        print(num,'*',i,'=',num*1)

def check_number():
    num = int(input('enter a number '))
    if (num>0):
        print('positive')
    elif (num<0):
        print('negative')
    else:
        print('zero')

def check_avg():
    arr = [1,2,3,4,5]
    avg =0
    for i in arr:
        avg += i
    avg /= len(arr)
    print(avg)

def fibonacci():
    num = int(input('enter a number '))
    a, b = 0,1
    print('Fibonacci Series:')
    for i in range(num):
        print(a, end=' ')
        a,b = b, a+b

def check_char():
    char = input('enter a character ')
    if(char.isalpha()):
        print('alphabet')
    elif(char.isdigit()):
        print('digit')
    else:
        print('special character')

def season():
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

def no_of_vowels():
    str = input('enter a string ')
    vowels = 0
    for i in str.strip():
        if i.lower() in 'aeiou':
            vowels += 1
    print('number of vowels in string are', vowels)

def calculator():
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

def greater_than():
    arr = [1,2,3,4,5]
    num = int(input('enter number '))
    for i in arr:
        if i>num:
            print(i)

def palindrome():
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

match x:
    case 1:
        t1=datetime.datetime.now()
        isprime()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 2:
        t1=datetime.datetime.now()
        divisible()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 3:
        t1=datetime.datetime.now()
        sum_even()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 4:
        t1=datetime.datetime.now()
        leap_year()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 5:
        t1=datetime.datetime.now()
        factorial()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 6:
        t1=datetime.datetime.now()
        no_of_words()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 7:
        t1=datetime.datetime.now()
        largest()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 8:
        t1=datetime.datetime.now()
        day_of_week()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 9:
        t1=datetime.datetime.now()
        number_reverse()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 10:
        t1=datetime.datetime.now()
        check_letter()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 11:
        t1=datetime.datetime.now()
        multiplication_table()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 12:
        t1=datetime.datetime.now()
        check_number()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 13:
        t1=datetime.datetime.now()
        check_avg()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 14:
        t1=datetime.datetime.now()
        fibonacci()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 15:
        t1=datetime.datetime.now()
        check_char()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 16:
        t1=datetime.datetime.now()
        season()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 17:
        t1=datetime.datetime.now()
        no_of_vowels()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 18:
        t1=datetime.datetime.now()
        calculator()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 19:
        t1=datetime.datetime.now()
        greater_than()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)
    case 20:
        t1=datetime.datetime.now()
        palindrome()
        t2=datetime.datetime.now()
        print('time taken :', t2-t1)