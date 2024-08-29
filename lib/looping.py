#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    # pass
    i = 11
    while i>1:
        i -= 1
        print (i)
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    # pass
    # squared = [ ]
    # for i in int_list:
    #     squared.append(i*i) 
    return [num ** 2 for num in int_list]

def fizzbuzz():
    # code goes here!
    # pass
     results= [
         'FizzBuzz' if num % 3 == 0 and num % 5 == 0
          else 'Fizz' if num % 3 == 0
          else 'Buzz' if num % 5 == 0
          else num
          for num in range(1, 101)
    ]
     for result in results:
        print(result)
