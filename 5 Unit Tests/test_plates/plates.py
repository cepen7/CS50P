import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(c):
    alphabet = list(string.ascii_uppercase)
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def first_two_letters(d): # checks if first two chars are letters
        if d[0] in alphabet and d[1] in alphabet:
            return True

    def no_interpunction(e): # makes sure only numbers and letters are used
        is_ok = True
        for dot in e:
            if dot not in alphabet and dot not in numbers:
                is_ok = False
        return is_ok

    def zero_not_first(f): #makes sure first no. is not a zero and
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

    if 2 <= len(c) <= 6: # length
        if first_two_letters(c) and no_interpunction(c) and zero_not_first(c): # checks all conditions
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()
