import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo0(self):
        print("Fixture Demo0")

    def test_fixtureDemo1(self):
        print("Fixture Demo1")

    def test_fixtureDemo2(self):
        print("Fixture Demo2")

    def test_fixtureDemo3(self):
        print("Fixture Demo3")
