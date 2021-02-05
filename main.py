"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
def summation(first_number, second_number):
    """Calculate the sum of 2 numbers provided by the user
    
    Args:
        first_number(int or float): first number
        second_number(int or float): second number
        
    Returns:
        int or float: sum of first_number and second_number
    """
    
    return(first_number + second_number)

print(summation(64,32))

# 3.- Make a program that prints a sentence that includes at least 3 variables.

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
