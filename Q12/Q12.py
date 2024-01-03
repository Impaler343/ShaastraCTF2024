
key = "ShaastraCTF{BoseEinstein}"
val = -273
x = 0
def response(x):
    diff = abs(val-x)
    if(diff < 5):
        return "Single digit on Kelvin scale"
    elif(diff < 10):
        return "freezing"
    elif(diff < 25):
        return "very cold"
    elif(diff < 50): 
        return "cold"
    
    elif(diff < 100):
        return "cool"
    elif(diff < 200):
        return "warm"
    elif(diff < 300):
        return "hot"
    elif(diff < 500):
        return "burning"
    else:
        return "You are on the sun"
print("Lets play a game of Cold and Hot :]")
while(x != val):
    print("Enter an integer")
    x = input()
    try:
        x = int(x)
        print(response(x))
    except:
        print("Please enter an integer")

print("Congrats on Solving , here is the flag: ")
print(key)