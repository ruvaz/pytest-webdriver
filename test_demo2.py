import pytest


@pytest.mark.smoke
@pytest.mark.skip ##skype test
def test_first_program(setup):
    msg = "Hello"
    assert msg == "Hi", "Test failed because string do not match"


def test_second_creditCard(setup):
    a = 4
    b = 2
    assert (a + 2) == 6, "Sum failed"



def test_fixtureDemo(setup):
    print("I'll execute steps in fixtureDemo method")