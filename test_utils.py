import gitactions_trial


def test_printhello():
    assert gitactions_trial.printhello() == "Hello_world"


def test_printWord():
    assert gitactions_trial.printWord("Potat") == "Potato"

    # Can't use pytest here because the time will change every second so it will always fail. So
    # I added the python file to gitactions after running the pytest is passed. I can make the pytest work here
    # but I have to use the now() function in the pytest instead of particular time in which the code was implemented.
    # But I don't need to since github actions is also checking the main file for errors.
    # def test_trial():
    #     test = ('Hello world!', 'Current date and time is ', 'Monday, 30-11-2020 : 14:53')
    #     assert trial() == test
