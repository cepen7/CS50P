def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

import string
alphabet = list(string.ascii_uppercase)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def is_valid(c):
    if 2 <= len(c) <= 6: # length
        if start(c) and dots(c) and nums(c):
            return True

def start(d): # checks if first two chars are letters
     if d[0] in alphabet and d[1] in alphabet:
          return True

def dots(e): # makes sure only numbers and letters are used
    is_ok = True
    for dot in e:
          if dot not in alphabet and dot not in numbers:
               is_ok = False
    return is_ok

def nums(f): #makes sure first no. is not a zero and
    number_present = False # that a letter is not preceded by a number
    for char in f[2:]:
        if char in numbers:
            if char == "0" and number_present == False:
                return False
            else:
                number_present = True
        if char in alphabet and number_present:
            return False

    return True



main()
