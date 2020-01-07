"""
Problem: Go through string to see if any characters are repeated
input: string
output: boolean
Examples: 
uniqueChars('ABC') == true
uniqueChars('AAB') == false
uniqueChars('Aa') == true
uniqueChars('') == None

Data Structure: Dictionary & Lists
Algorithm: 
0: If input length is 0 then return None
1: Check to see if character is in dictionary
    I: if not store in string into a dictionary as properties with a value of 1
    II: If character already lives on dictionary, increment property value
    
2: Loop through dictionary and check to see if any values are greater than 1
3: If any values are greater than 1 return false, otherwise return true
"""

def uniqueChars(string):
    if(len(string) == 0):
        return None
    charCount = {}
    for char in string:
        if char in charCount:
            return False
        else:
            charCount[char] = 1
    for char in charCount:
        if len(char) > 1:
            return True