import time

d = {'#':'1', '@':'2', '?':'3', '!':'4', '^':'5', ':':'6', '*':'7', '%':'8', '$':'9', '+':'0'}


def compare_strings(string1, string2):
    if len(string1) != len(string2):
        print("Nope, Wrong Password?")
        return

    for char1, char2 in zip(string1, string2):
        if d[char1] != char2:
            print("Nope, Wrong Password?")
            return

        time.sleep(1)

    print("Nope, Wrong Password?")


password1 = "%?^*%$@!:#"


do = input("Press 'ok' to start the game:")
while do == "ok":
    password2 = input("Enter a 10 digit password consisting of numbers only:")
    compare_strings(password1, password2)
    do = input("Press 'ok' to try again!")
