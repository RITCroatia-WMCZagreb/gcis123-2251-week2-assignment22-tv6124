'''
@ASSESSME.USERID: tv6124
@ASSESSME.AUTHOR: Tyra Vladić
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''
def add_chars(char1, char2):
    value = ord(char1)
    value1 = ord(char2)
    result = value + value1
    print("Adds up to: ", result, "The character is: ", chr(result))
    


def subtract_chars(char1, char2):
    value = ord(char1)
    value1 = ord(char2)
    result = value - value1
    print("The difference is: ", str(result) , ", and the character is: " , chr(result))


def main():
    char1 = input("Please enter the first character: ")
    char2 = input("Please enter the second characcter: ")
    add_chars(char1, char2)
    subtract_chars(char1, char2)
    
if __name__ == "__main__":
    main()


