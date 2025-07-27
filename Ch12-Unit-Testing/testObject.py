#pip install pylint
#pylint ./testObject.py

aVar = 1
B_VAR = 2
print(aVar)
print(B_VAR)

def capitalize(s: str) -> str:
    '''
    Input a String
    Capitalize the first letter of the string
    :param s: input string
    :return: capitalized string
    '''
    return s.capitalize()