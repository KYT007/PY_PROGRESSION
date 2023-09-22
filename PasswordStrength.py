'''Here we have anothe practice project from Al Swaigert's book "Automate The Boring Stuff With Python".
This is also a project from chapter 7 called Password Strength. The reader is assigned to write a function
that takes input from a user that is a make-believe "password" and checks the user's input against a regex 
(or as hinted, multiple regexes) to test the strength of the password. As the book states it, a strong password
is defined as being at least 8 characters long, contains upper and lowercase letters, and contains at least one digit.
I've gone ahead and taken the liberty of putting in one more requirement: a special character such as !, #, or something
similar, just to make things interesting. '''

import re # Firstly we import our re module. This allows us to use regex patterns.

#the primary function
def password_strength():
    patterns = [ r'\d+', r'\w+', r'[A-Z]+', r"(?:[a-zA-Z].*){8,}"]
    '''Here are our regex patterns. I don't know why, but I ended up making TWO different
    regexes for word characters/letters: one regex that simply detects them, and another regex that checks if there
    are at least 8 characters. I could very well have combined these two but didn't.'''
    
    '''Set this up with a while loop and an input function so the user can keep trying different passwords infinitely.
    Figured this would make this practice project a little less tedious to test.'''
    while True:
        to_be_tested = input('Please enter a password: ') # Our variable we assign the input that is our "password" to.
        matches = 0 #For every regex item found in our password, "macthes" goes up by one.
        #Matches will be what we use to rank our password stegnth.
        for regexpattern in patterns: #We use a for loop and test our input variable against the regex patterns.
            if re.search(regexpattern, to_be_tested):
                matches += 1
        if matches == 1:
            print('weak password')  # We use some basic if and elif flow control statements to check our password
        elif matches == 2:
            print('password is medium strength')
        elif matches == 3:
            print('Password is good')
        elif matches == 4:
            print('Password strength is strong')
    
    
password_strength() # We call the function to use it.