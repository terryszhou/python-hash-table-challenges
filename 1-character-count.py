'''
1. Character Count:
given a string count each letter in the string and then print the result.

Example 1:

character_count('banana')

Input: 'banana'
Output (in the console): 
the character b occurs 1 times
the character a occurs 3 times
the character n occurs 2 times

Example 2:

character_count('hello world')

Input: 'hello world'
Output (in the console): 
the character h occurs 1 times
the character e occurs 1 times
the character l occurs 3 times
the character o occurs 2 times
the character   occurs 1 times
the character w occurs 1 times
the character r occurs 1 times
the character d occurs 1 times
'''

def character_count(string):
    hash = {}
    for char in string:
        if char in hash: hash[char] += 1
        else: hash[char] = 1
    
    for i in hash:
        result = f"The character {i} occurs {hash[i]} time"
        print(result + ".") if hash[i] == 1 else print(result + "s.")

character_count("banana")