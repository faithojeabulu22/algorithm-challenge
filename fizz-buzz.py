"""
Author:faith ojeabulu 
Date:10th october 2020 



Question: Write a program that returns a list of all the numbers from 1 to an integer argument. 
But for multiples of three use “Fizz” instead of the number and for the multiples of five use 
“Buzz”. For numbers which are multiples of both three and five use “FizzBuzz". """





def fizz_buzz(maximum):
    lst =[]
    for i in range(1, maximum + 1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append("FizzBuzz")
        elif i % 3 == 0:
            lst.append("Fizz")
        elif i % 5 == 0:
            lst.append("Buzz")
        else:
            lst.append(i)
    return lst  

print(fizz_buzz(15))