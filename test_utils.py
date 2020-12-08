import gitactions_trial
import datetime


def test_printhello():
    assert gitactions_trial.printhello() == "Hello_world"


def test_printWord():
    assert gitactions_trial.printWord("Spud") == "Potato"

    # Can't use pytest here because the time will change every second so it will always fail. So
    # I added the python file to gitactions after running the pytest is passed. I can make the pytest work here
    # but I have to use the now() function in the pytest instead of particular time in which the code was implemented.
    # But I don't need to since github actions is also checking the main file for errors.

def test_trial():
    now = datetime.datetime.now()
    test = ('Hello World', 'Current date and time is', now.strftime("%A, %d-%m-%Y : %H:%M"))
    assert gitactions_trial.trial("Hello World", "Current date and time is", now) == test
