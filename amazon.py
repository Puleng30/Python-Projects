
'''Initially I got this error when I was trying to define min and max functions:
"return min(numbers) [Previous line repeated 996 more times. 
RecursionError: maximum recursion depth exceeded". I then used the recursive function 
to check if the input list has only 1 element. What the recursive function does is, if the list 
only has 1 element then it returns that element; otherwise it compares the first element of 
the list with the min/max of the rest of the list. It does so by calling the 
recursive_min/recursive_max function recursively with the rest of the list.'''
def recursive_min(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return min(numbers[0], recursive_min(numbers[1:]))

def recursive_max(numbers):
    if len(numbers) == 1:
        return numbers [0]
    else:
        return max(numbers[0], recursive_max(numbers[1:]))

def avg(numbers):  #defining the average function 
    return sum(numbers) / len(numbers)   #calculating the average of the numbers

with open('input.txt', 'r') as file:    # Opening the input file to be read
    results = {}   # Initialising a dictionary to hold the results

    for line in file:     #using the for loop to loop through each line in the file
        '''Using the strip and split functions to strip and split the line into the 
        operation and the list of numbers'''
        operation, numbers_str = line.strip().split(':')     
        numbers = [int(x) for x in numbers_str.split(',')]

        if operation == 'min':
            result = min(numbers)
        elif operation == 'max':
            result = max(numbers)
        elif operation == 'avg':
            result = avg(numbers)

        results[operation] = result   #adding the results to the dictionary

with open('output.txt', 'w') as f:    #opening the output file to be written into 
    f.write(f"The min of {numbers} is {results['min']}.\n")  #writing the results to the file
    f.write(f"The max of {numbers} is {results['max']}.\n")  #writing the results to the file
    f.write(f"The avg of {numbers} is {results['avg']}.\n")  #writing the results to the file


