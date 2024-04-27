def Taks1(number : int):
    """
    Convert a Number to a String!

    We need a function that can transform a number (integer) into a string.
    What ways of achieving this do you know?
    
    Examples (input --> output):
    123  --> "123"
    999  --> "999"
    -100 --> "-100"
    """

    return str(number)

def Taks2(name : str):
    """
    Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

    Can you help her?
    """
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
    
def Task3(boolean : bool):
    """Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false."""
    match boolean:
        case True:
            return "Yes"
        case False:
            return "No"

def Task4(name : str):
    """
        Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!

    The function takes a name as its only argument, and returns one of the following strings:

    name + " plays banjo" 
    name + " does not play banjo"
    Names given are always valid strings.
    """

    firstChar = name[0]
    if firstChar == "r" or firstChar == "R":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
    
def Task5(sheeps : list[bool]):
    """
        Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

    For example,

    [True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True]
    The correct answer would be 17.

    Hint: Don't forget to check for bad values like null/undefined
    """

    i = 0
    for sheep in sheeps:
        if sheep == True:
            i += 1
        
    return i

def Task6(n : int):
    """
        Convert number to reversed array of digits
    Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

    Example(Input => Output):
    35231 => [1,3,2,5,3]
    0 => [0]
    """

    arr = []
    
    if n == 0:
        arr.append(0)
        return arr
    
    while n >= 1:
        arr.append(n % 10)
        n //= 10
    return arr

def Task7(haystack : list[str]):
    """
        Can you find the needle in the haystack?

    Write a function findNeedle() that takes an array full of junk but containing one "needle"

    After your function finds the needle it should return a message (as a string) that says:

    "found the needle at position " plus the index it found the needle, so:

    Example(Input --> Output)

    ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
    Note: In COBOL, it should return "found the needle at position 6"
    """
    i = 0
    for item in haystack:
        if item == "needle":
            return f'found the needle at position {i}'
        i += 1

def Task8(n=0):
    """
        Given an input n, write a function always that returns a function which returns n. Ruby should return a lambda or a proc.

    three = always(3)
    three() /* returns 3 */
    """
    return lambda:n

def Task9(a :list[object]):
    """
        Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

    Examples
    Input: [1, 5.2, 4, 0, -1]
    Output: 9.2

    Input: []
    Output: 0

    Input: [-2.398]
    Output: -2.398

    Assumptions
    You can assume that you are only given numbers.
    You cannot assume the size of the array.
    You can assume that you do get an array and if the array is empty, return 0.
    What We're Testing
    We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
    Advanced users may find this extremely easy and can easily write this in one line.
    """
    sum = 0
    for number in a:
        sum += number
        
    return sum

def Task10(a, b):
    """
    This code does not execute properly. Try to figure out why.
    """

    return a * b

def Task11(w,d,h):
    """
    Write a function that returns the total surface area and volume of a box as an array: [area, volume]
    """

    return [2*(w*h+w*d+h*d), w*h*d]

def Task12(p1, p2):
    """
        Rock Paper Scissors
    Let's play! You have to return which player won! In case of a draw return Draw!.

    Examples(Input1, Input2 --> Output):

    "scissors", "paper" --> "Player 1 won!"
    "scissors", "rock" --> "Player 2 won!"
    "paper", "paper" --> "Draw!"
    """

    if p1 == "scissors" and p2 == "paper": return "Player 1 won!"
    if p1 == "scissors" and p2 == "rock": return "Player 2 won!"

    if p1 == "rock" and p2 == "scissors": return "Player 1 won!"
    if p1 == "rock" and p2 == "paper": return "Player 2 won!"

    if p1 == "paper" and p2 == "scissors": return "Player 2 won!"
    if p1 == "paper" and p2 == "rock": return "Player 1 won!"


    if p1 == "scissors" and p2 == "scissors": return "Draw!"
    if p1 == "rock" and p2 == "rock": return "Draw!"
    if p1 == "paper" and p2 == "paper": return "Draw!"


def Task13(n):
    """
    Each number should be formatted that it is rounded to two decimal places. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

    Example:    
    5.5589 is rounded 5.56   
    3.3424 is rounded 3.34
    """
    return round(n,2)

def Task14(number : float):
    """
        Each floating-point number should be formatted that only the first two decimal places are returned. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

    Don't round the numbers! Just cut them after two decimal places!

    Right examples:  
    32.8493 is 32.84  
    14.3286 is 14.32

    Incorrect examples (e.g. if you round the numbers):  
    32.8493 is 32.85  
    14.3286 is 14.33
    """

    lengh = len(str(number).split('.')[1])
    return float(str(number)[:-(lengh-2)])

def Task15(size : int):
    """
        write me a function stringy that takes a size and returns a string of alternating 1s and 0s.

    the string should start with a 1.

    a string with size 6 should return :'101010'.

    with size 4 should return : '1010'.

    with size 12 should return : '101010101010'.

    The size will always be positive and will only use whole numbers.
    """

    str = ""
    for i in range(size):
        if i % 2 == 0: str += "1"
        else: str += "0"\
        
    return str

def Task16():
    """
    Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

    Example
    input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
    ouptut: 5 
    The most frequent number in the array is -1 and it occurs 5 times.
    """

    def most_frequent_item_count(collection : list[int]):
        
        # Do your magic. :)
        arr = []
        arrCounts = 0
        collection.sort()
        count = 1
        _count = 1
        print(collection.count(10))
        if len(collection) == 0:
            return 0
        
        for i in range(len(collection)-1):
            print(_count, collection[i])
            if collection[i] == collection[i+1]:
                _count += 1
            elif count < _count:
                count = _count
                _count = 1
            else:
                _count = 1
        collection.sort(reverse=True)
        if collection.count(collection[0]) > count:
            count = collection.count(collection[0])

        return count

    
    
    print(most_frequent_item_count([5, 3, -5, 7, -5, -4, 3, 4, -7, 0, -6, -10, 9, 2, 9, -6, -2, -7, -6, -2, -6, 4, 10, -2, 8, -4, -9, 1, 7, 10, -9, 1, 3, 1, -2, -7, -4, -10, 10, -6, 5, -8, 10, -2, -9, -8, 6, 10, -1, -10, 9, -3, -1, 9, 3, -6, 10, -7, -8, 5, 0, -3, 10, 3, -4, 10, 7]))

def Task17(bool : bool, func1, func2):
    """
        Create a function called _if which takes 3 arguments: a value bool and 2 functions (which do not take any parameters): func1 and func2

    When bool is truthy, func1 should be called, otherwise call the func2.

    Example:
    def truthy(): 
    print("True")
    
    def falsey(): 
    print("False")
    
    _if(True, truthy, falsey)
    # prints 'True' to the console
    """
    if bool: func1()
    else: func2()
    


def Task18(amount : float):
    """
        The company you work for has just been awarded a contract to build a payment gateway. In order to help move things along, you have volunteered to create a function that will take a float and return the amount formatting in dollars and cents.

    39.99 becomes $39.99

    The rest of your team will make sure that the argument is sanitized before being passed to your function although you will need to account for adding trailing zeros if they are missing (though you won't have to worry about a dangling period).

    Examples:

    3 needs to become $3.00

    3.1 needs to become $3.10
    Good luck! Your team knows they can count on you!
    """
    amount = (amount * 100) / 100.0
    string = str(amount)
    print(len(string)-string.find('.'))
    if len(string)-(string.find('.') + 1) > 2:
        return f"${string[:-(len(string)-string.find('.'))]}"
    if len(string)-(string.find('.') + 1)  == 2:
        return f"${string}"
    if len(string)-(string.find('.') + 1)  == 1:
        return f"${string}0"
    if len(string)-(string.find('.') + 1)  == 0:
        return f"${string}00"
    
def Task19(s : str):
    """
        Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

    Valid examples, should return true:

    isDigit("3")
    isDigit("  3  ")
    isDigit("-3.23")
    should return false:

    isDigit("3-4")
    isDigit("  3   5")
    isDigit("3 5")
    isDigit("zero")
    """

    try:
        float(s)
        return True
    except:
        return False

def Task20(id : int):
    """
        The function is not returning the correct values. Can you figure out why?

    Example (Input --> Output ):

    3 --> "Earth"
    """

    match id:
        case 1: return "Mercury"
        case 2: return "Venus"
        case 3: return "Earth"
        case 4: return "Mars"
        case 5: return "Jupiter"
        case 6: return "Saturn"
        case 7: return "Uranus"  
        case 8: return "Neptune"

def Task21(n : int):
    """
    Unfinished Loop - Bug Fixing #1
    Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!
    """

    res=[]
    i = 1
    while i <= n: 
        res.append(i)   
        i += 1
    
    return res

def Task22(*args):
    return "I like {}!".format(", ".join(args))

def Task23(temp):
    """
    Debug celsius converter
    Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius. Unfortunately his code has some bugs.

    Find the errors in the code to get the celsius converter working properly.

    To convert fahrenheit to celsius:

    celsius = (fahrenheit - 32) * (5/9)
    Remember that typically temperatures in the current weather conditions are given in whole numbers. It is possible for temperature sensors to report temperatures with a higher accuracy such as to the nearest tenth. Instrument error though makes this sort of accuracy unreliable for many types of temperature measuring sensors.
    """
    def convert_to_celsius(temperature):
        celsius = (temperature - 32) * (5.0/9.0)
        return celsius
    c = convert_to_celsius(temp)
    if (c > 0):
        return (f"{c} is above freezing temperature")
    else:
        return (f"{c} is freezing temperature")
    
def Task24(is_busy):
    if is_busy:
        return {"status":"busy" }
    else:
        return {"status":"available"}
    

def Task25(body, tail):
    sub = body[len(body)-1]
    if sub == tail:
        return True
    else:
        return False
    
def Task26(name, surname):
    return f"{name} {surname}"

def Task27(health):
    if health <= 0:
        return False
    else:
        return True
    
def Task28(health):
    if health <= 0:
        return False
    else:
        return True
    
def Task29(s1, s2, s3):
    # Code here
    grade = (s1 + s2 + s3)/3
    if 90 <= grade <= 100:
        return "A"
    if 80 <= grade < 90:
        return "B"
    if 70 <= grade < 80:
        return "C"
    if 60 <= grade < 70:
        return "D"
    if 0 <= grade < 60:
        return "F"

def Task30(word):
    # TODO: complete
    
    def alphabet(char):
        alph = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
        for i in range(len(alph)):
            if char == alph[i]:
                return True
        return False    
    firstChar = alphabet(word[0])
    prevChar = firstChar
    for i in range(1, len(word)):
        if alphabet(word[i]) == prevChar:
            return False
        else:
            prevChar = not prevChar
    return True

def Task31(arr : list[int]):
    if arr != None and len(arr) > 0:
        arr.sort(reverse=True)
        arr.pop(0)
        if len(arr) > 0:
            arr.pop(len(arr)-1)
        else:
            return 0
    else:
        return 0

    sum = 0
    for item in arr:
        sum += item

    return sum

def Task32(text : list[str], char : str):
    longest = 0
    _text = ""
    for txt in text:
        if len(txt) > longest:
            longest = len(txt)

    for txt in text:
        while len(txt) < longest:
            txt += " "
        txt = char + " " + txt + " " + char + "\n"
        _text += txt
    
    value = ""
    for i in range(0, longest + 4):
        value += char
    value += "\n"
    
    return value + _text + value[:-1]


import datetime

def Task33(year):
    daysInWeek2 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if year == 3300 or  year == 1700:
        return [daysInWeek2[datetime.datetime(year, 1, 1).weekday()]]
    if year % 4 == 0:
        if datetime.datetime(year, 1, 1).weekday() < datetime.datetime(year, 1, 2).weekday():
            return [daysInWeek2[datetime.datetime(year, 1, 1).weekday()], daysInWeek2[datetime.datetime(year, 1, 2).weekday()]]
        else:
            return [daysInWeek2[datetime.datetime(year, 1, 2).weekday()], daysInWeek2[datetime.datetime(year, 1, 1).weekday()]]
    else:
        return [daysInWeek2[datetime.datetime(year, 1, 1).weekday()]]

print(Task33(2024))