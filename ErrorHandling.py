try:
    num = int(input("Enter a number: "))
    result = 10/num
    answer = 'result =' + result
    print(undeclared_variable)
    num.append(5)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")

except TypeError:
    print("Cannot add integer and string")

except NameError:
    print(" Name error: variable is not defined.")

except AttributeError:
    print('Error : object does not support this error')

except Exception as e:
        print(f" An unexpected error occurred: {e}")

else:
    print('result =',result)

finally:
     print("error handling completed successfully")