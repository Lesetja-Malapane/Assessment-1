def grade_average(grades:list):
    """ Write a program that returns the average number of a given list of grades.
    It should not add any negative grades to the average.

    Args:
        grades (list): List of grades to calculate
    """

    average = 0

    for digit in grades:
        if digit < 0:
            grades.remove(digit)

    for number in grades:

        if number >= 0:
            average = average + number
            continue
            
        elif number < 0:
            grades.remove(number)
            continue
            
        else:
            continue
        
    if average > 0:
        return (average)/(len(grades))
    else:
        return average

def find_prime_factors(number):
    """Write code to return the prime factors of the number. 

    Args:
        number (int): Number to find the prime factors of
    """

    for digit in range(1, number):
        if   


def calculate_interest(principal, rate, years):
    """Write a program that returns the compound interest

    Args:
        principal (int): The principal amount
        rate (int): The interest rate
        years (int): The amount of years to calculate the interest for
    """


def code_word(code):
    """Write a program that returns the word given a code.

    e.g. Given code: [3,1,20]
    Expected Word: "cat"

    Args:
        code (list): The code to decipher
    """

    letter = {
        0: " ",
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h",
        9: "i",
        10: "j",
        11: "k",
        12: "l",
        13: "m",
        14: "n",
        15: "o",
        16: "p",
        17: "q",
        18: "r",
        19: "s",
        20: "t",
        21: "u",
        22: "v",
        23: "w",
        24: "x",
        25: "y",
        26: "z"
    }

    string = ""

    for number in code:
        string = string +letter[number]

    return string

def triangles(length):
    """Write a program that returns a triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    ***
    ****
    *****

    Args:
        length (int): The ;ength your triangle should be
    """


def hollow_triangle(length):
    """Write a program that returns a hollow triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    * *
    *  *
    *****

    Args:
        length (int): The ;ength your triangle should be
    """


# There are no tests for this function so test by running the program. 
def number_guessing(number):
    """Write a guessing game. The player has 10 opprtunites to guess.

    e.g. Number: 4
         User Input: 5
         Output: Incorrect

         Number: 4
         User Input: 4
         Output: Correct

    Args:
        number (int): The number to be guessed
    """

