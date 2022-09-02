#Create a Function to check if a string is a palindrome
def isPalindrome(string):
    #Store the string in a list
    stringList = list(string)
    #Store the length of the string in variables
    length = len(stringList)
    newLength = length
    #Make a list that'll store the reversed string
    revString = []
    #Go through every letter in string
    for i in range(length):
        #Take that last letter of the string and put it in revString
        lastLetter = stringList.pop(newLength-1)
        revString.append(lastLetter)
        #Store the new length of the string
        newLength = len(stringList)
    #Join the two lists together as a string
    revString = "".join(revString)
    #Return True or False if the string is a palindrome
    if (string == revString): return(True)
    else: return(False)
