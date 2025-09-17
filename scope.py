'''
@ASSESSME.USERID: tv6124
@ASSESSME.AUTHOR: Tyra Vladic
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL = "Cats and dogs"
INT_GLOBAL = 205
FLOAT_GLOBAL = 2.005

def print_param(parameter):
    print("The parameter value is:", parameter)


def print_local():
    local_1 = "Helloooo"
    print("Local: ",  local_1)

def print_which():
    STRING_GLOBAL = 2000
    print("Local STRING_GLOBAL is: ", STRING_GLOBAL)

def main():
    print_param(STRING_GLOBAL)
    print_param(INT_GLOBAL)
    print_param(FLOAT_GLOBAL)

if __name__ == "__main__" :
    main()

