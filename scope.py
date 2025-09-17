'''
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL = "Hello"
INT_GLOBAL = 42
FLOAT_GLOBAL = 3.14

def print_param(parameter):
    print("Parameter value: ",parameter)

def print_local():
    local_variable = "I am local"
    print("Local variable value: ",local_variable)

def print_which():
    STRING_GLOBAL = "Shadowed!"
    print("Local STRING_GLOBAL inside print_which():", STRING_GLOBAL)


def main():
    print_param(STRING_GLOBAL)
    print_param(INT_GLOBAL)
    print_param(FLOAT_GLOBAL)
    local_variable = "Different local value"
    print_local()
    print_which()
    print("Global STRING_GLOBAL after print_which():", STRING_GLOBAL)

if __name__ == "__main__":
    main()