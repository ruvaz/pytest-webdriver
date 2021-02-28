import pytest


@pytest.mark.smoke
def test_firstprogram(setup):
    msg = "Hello"
    assert msg == "Hi"


@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Goog Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
