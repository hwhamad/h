#Create a Function that take a string as a list and reverses it
def reverseString (string):
    #Store the length of the string in variables
    length = len(string)
    newLength = length
    #Make a list that'll store the reversed string
    revString = []
    #Go through every letter in string
    for i in range(length):
        #Take that last letter of the string and put it in revString
        lastLetter = string.pop(newLength-1)
        revString.append(lastLetter)
        #Store the new length of the string
        newLength = len(string)
    #Return the reversed string as a list
    return(revString)
