
import math                                     #importing the math module 

numbers =[]                                     #this block of code requests the user to input 10 floats. the entered numbers get appended to a list called numbers
for x in range(10): 
    try:
         number = float(input("Enter a number: ")) 
         numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid float")

total_of_all_numbers = sum(numbers)             #finding the total of all numbers entered using the sum function and storing the value in a variable called total_of_all_numbers
print('The total of all numbers is: ', total_of_all_numbers)

index_of_maximum = numbers.index(max(numbers))  #finding the index of the maximum using the max function and storing the value in a variable called index_of_maximum
print("The index of the maximum is: ", index_of_maximum)

index_of_minimum = numbers.index(min(numbers))  #finding the index of the minimum using the min function and storing the value in a variable called index of minimum
print("The index of the minimum is: ", index_of_minimum) 

average = sum(numbers) / len(numbers)           #calculating the average of the numbers and rounding off to 2 decimal places and storing the value in a variable called average
average = round(average, 2)
print("The average of the numbers is: ", average)

numbers_sorted = sorted(numbers)                #finding the median number using the sorted function.
median_ = len(numbers) // 2                     
if len(numbers) % 2 == 0:                       #checking to see if the length of the list is even or odd
    median = (numbers_sorted[median_ - 1] + numbers_sorted[median_]) / 2    #this code is if the length of the list is even. in which case the median is calculated by finding the average of the middle two numbers
else:
    median = numbers_sorted(median_)                                        #if the length of the list is odd, the median is calculated by taking the middle number
print("Median number is: ", median)