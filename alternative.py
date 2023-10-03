
#Program that reads in a string and alternates the case of each character. 
def alternative_scenario(sentence):             #sentence is the string that will be modified
    a_new_sentence = ""                         #this is an empty string which will be used to build the changed string
    upper = True                              
    for x in sentence:                          #this for function will loop through all the characters in the string/sentence 
        if x.isalpha():                         #if x is an alphabet, the for function will check if it is upper or lower case. if x is upper meaning upper = True, then x will be added to the new_sentence in upper case. if x is lower meaning upper = False, then x will be added as a lower case
            if upper:
                a_new_sentence += x.upper()     #using the .upper() function to make the charaters upper case 
            else:
                a_new_sentence += x.lower()     #using th .lower fuction to make the characters lower case
            upper = not upper                   #this function makes sure that the next alphabetic character is in the opposite case
        else:
            a_new_sentence += x
    return a_new_sentence

#Showing an example 
sentence = "It's raining and cold today."
a_new_sentence = alternative_scenario(sentence)
print(a_new_sentence)  

#Program that alternates the case of each word
def alternative_expression_scenario(sentence):    #sentence is the string that will be modified
    a_new_sentence = ""                           #this is an empty string which will be used to build the changed string
    expression = sentence.split()                 #spliting sentence using the split function and storing it into a variable called expression
    upper = True                                  #this fuction will make the first word in the sentence to be upper case
    for b, expression in enumerate(expression):   #the for funtion will loop through every word in the expression list. the enumerate function keeps track of the index of each word in the list
        if b % 2 == 0:                            #if the modulus of b is 0, meaning b is even, the function will add the word to the new_sentence variable in lower case using the lower case function. if b is odd then it will be added in upper case using the upper fuction
            a_new_sentence += expression.lower()
        else:
            a_new_sentence += expression.upper()
        a_new_sentence += " "                      #the += character adds space after the current word is added to the new_sentence. this makes sure that there are spaces between words in the sentence
    return a_new_sentence.strip()                  #the strip function removes any extra spaces that might be in the new sentence

#Showing an example 
sentence = "Seasons are definately changing!"
a_new_sentence = alternative_expression_scenario(sentence)
print(a_new_sentence)  