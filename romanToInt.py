#Create a Function that converts a roman numeral into an integer
def romanToInt(numeral):
    #Make a Dictionary that stores the value of every roman numeral
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    #Make a variable that'll store the final value
    value = 0
    #Create lists to for whatever values to subtract from
    subISymbols = ["V","X"]
    subXSymbols = ["L","C"]
    subCSymbols = ["D","M"]
    #Go through every symbol in the roman numeral
    for i in range(len(numeral)):
        #Store the value of the symbol and the next symbol
        symbol = numeral[i]
        if (i != (len(numeral) - 1)): nxtSymbol = numeral[i+1]
        #Check for Subtracting Symbols and subtract if necessary
        if (symbol == "I" and (nxtSymbol in subISymbols)):
            value -= 1
        elif (symbol == "X" and (nxtSymbol in subXSymbols)):
            value -= 10
        elif (symbol == "C" and (nxtSymbol in subCSymbols)):
            value -= 100
        else:
            #If it isn't a subtracting symbol add the value
            value += roman[symbol]
    #Return the final value
    return(value)
