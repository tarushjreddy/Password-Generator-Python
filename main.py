import string
import random
if __name__ == "__main__":
    setone = string.ascii_uppercase
    settwo = string.ascii_lowercase
    setthree = string.digits
    setfour = string.punctuation
    # print(setone)
    # print(settwo)
    # print(setthree)
    # print(setfour)

    plen = int(input("Enter the password the length\n"))
    s = []
    s.extend(list(setone))
    s.extend(list(settwo))
    s.extend(list(setthree))
    s.extend(list(setfour))
    random.shuffle(s)
    # print(s)
    print("".join(s[0:plen]))
