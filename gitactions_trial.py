import datetime

def printhello():
    return "Hello_world"

def printWord(word):
    return word

def trial(word, d, time):
    print("Hello world!")
    print("Current date and time is ")
    t = time.strftime("%A, %d-%m-%Y : %H:%M")
    print(t)
    
    return word, d, t

print(trial("Hello World", "Current date and time is", datetime.datetime.now()))
