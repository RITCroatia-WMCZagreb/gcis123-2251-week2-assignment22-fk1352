'''
@ASSESSME.USERID: Faris Karić , fk1352
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''
def add_chars(char1, char2):
    total = ord(char1) + ord(char2)
    print("Sum of ASCII values: ",total)
    print("Associated ASCII character: ",chr(total % 128))

def subtract_chars(char1, char2):
    difference = ord(char1) - ord(char2)
    print("Difference of ASCII values: ",difference)
    if 0 <= difference <= 1000:
        print("Associated ASCII character:", chr(difference))
    else:
        print("No valid ASCII charactzer for this difference")

def main():
    first = input("Enter first character: ")
    second = input("Enter second character: ")
    add_chars(first, second)
    subtract_chars(first, second)

if __name__ == "__main__":
    main()

#COMMENT1: when i type the first and second character for ex. q and M, I don't see any unusual things other than 
#           associated characters which are > and $ .
#COMMENT2: when I type more than two characters, some unusual errors occur stating that the def main is incorrect or
#           something like that. 
# When I did the assignment I didnt have access to internet for some reason so I couldn't research the problem on google, sorry...
#           Will check the problem at school during the week...