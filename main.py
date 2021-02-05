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

def homework_reminder(class_name, assignment_number, day_of_week, time_of_day):
    """Returns a reminder for students showing the date and time that a homework assignment is due.

    Args:
        class_name(str): Name of class
        assignment_number(int): Assignment number
        day_of_week(str): Day of the week that the assignment is due
        time_of_day(float): Time of the day that the assignment is due (24 hour clock)
        
    returns:
        str: Homework reminder.

    """
    
    message = "This is a reminder that your " + class_name + " homework assignment #" + str(assignment_number) + " is due this " + day_of_week + " at " + str(time_of_day) + "." #creates variable called 'message', converts integer and float variables to strings.
    return message

print(homework_reminder("Python", 1, "Sunday", 14.25))


# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."

def sentence_length(sentence):
    """Return the number of characters in a sentence provided by user

    Args:
        sentence(str): Sentence provided by user
    
    Returns:
        int: number of characters in sentence
        
    """
    
    return len(sentence)

print(sentence_length("This is my first Python program."))


# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"

def overscan(width_resolution, height_resolution):
    """Returns a string with the 10% over-scan values of an inputted screen resolution

    Args:
        width_resolution(float): Height screen resolution
        height_resolution(float): Width screen resolution
        
    Returns:
        str: "The 10% overscan of 1920 is <width_resolution>, and the 10% overscan of 1080 is <height_resolution>"
        
    """
    
    overscan_width = int(width_resolution * 0.1) # Calculate 10% of width_resolution, converts to integer
    
    overscan_height = int(height_resolution * 0.1) # Calculate 10% of height_resolution, converts to integer
    
    message = "The 10% overscan of 1920 is " + str(overscan_width) + " and the 10% overscan of 1080 is " + str(overscan_height) + "." # Creates message variable and converts integer variables into strings
    return message

print(overscan(1920, 1080))
