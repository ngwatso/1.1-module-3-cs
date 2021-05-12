def csLongestPossible(str_1, str_2):
    newStr = ""
    
    for char in str_1:
        if char in newStr:
            continue
        else:
            newStr += char
    for char in str_2:
        if char in newStr:
            continue
        else:
            newStr += char
    strList = sorted(list(newStr))
    
    return ''.join(strList)

'''

U:

str_1 = "abcdefg"
str_2 = "aabbccz"
output = "abcdefgz"

str_1 = "bob"
str_2 = "barbara"
output = "abor"

str_1 = "abcdef"
str_2 = "ghijkl"
output = "abcdefghijkl"

P:

create a new string, add str_1 and str_2 to new string, minus duplicates,sort new string 
'''

# ==============================================

def csSortedTwoSum(numbers, target):

    i = []
    
    for n in numbers:
        num = target - n
        if num in numbers:
            i.append(numbers.index(n))
            i.append(numbers.index(num))
            return i
        else:
            continue
            
'''

U:

[1, 2, 3, 4, 5]
target = 4
output = [0, 2]

[3, 6]
target = 9
output = [0, 1]

P:

create var num, create list i; iterate through numbers, subtract 1st number from target; save result to num.  if num is in numbers, save it's index and 1st number's index to i.  otherwise, continue to iterate. 
'''

# ==============================================

def csFindAddedLetter(str_1, str_2):
    
    for i in str_2:
        if str_2.count(i) > str_1.count(i):
                return i
        else:
            continue


'''

U:

str_1 = "abcdef"
str_2 = "dbagcfe"
output = "g"

str_1 = "a"
str_2 = "aa"
output = "a"

str_1 = ""
str_2 = "a"
output = "a"

P:

iterate through str_2, if count of i is greater in str_2 than str_1, return i
'''

# ==============================================

def csFirstUniqueChar(input_str):
    
    
    # if input_str == "" or input_str[1:-1] == input_str[0]: # O(n)
    #     return -1
    # else:
    #     for i in input_str: # O(n)
    #         if input_str.count(i) == 1: # O(n)
    #             return input_str.index(i) # O(1)
    #         else: # O(1)
    #             continue  
    
    # if len(input_str) > 0:
    #     for i in input_str: # O(n)
    #         if input_str.count(i) > 1: # O(n)
    #             if input_str.count(i) == len(input_str):
    #                 return -1
    #             else:
    #                 continue
    #         else: # O(1)
    #                 return input_str.index(i) # O(1)
    # else:
    #     return -1
    
    occurences = {}
    
    for i in input_str:
        if i not in occurences:
            occurences[i] = 1
        else:
            occurences[i] +=1
    for key, value in occurences.items():
        if value == 1:
            return input_str.index(key)
    return -1
    
    # Runtime: O(n^c)
    # Space: O(1)

'''

U:

"lambdaschool"
output = 2

""
output = -1

"pepsi is pep"
output = 0

P:

if string is empty, return 0, otherwise iterate through string, if count of i is greater than 1, continue, if count of i is 1, return i, if no unique characters, return -1

'''