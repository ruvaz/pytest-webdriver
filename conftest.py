import pytest


@pytest.fixture(scope="class")  # class sirgve para indicar que se cargara una sola vez en una class
def setup():
    print("\n>I'll e executing first")
    yield
    print("\n>I'll be executed at last")


@pytest.fixture()
def dataLoad():
    print("\n>User data has been created")
    return ["Ruben", "Vazquez", "Ramirez"]


# parametros que van a hacer que un test se ejecute con cada uno de estos valores
@pytest.fixture(params=[("chrome","ruben"), "firefox", "edge"])
def crossBrowser(request):
    return request.param
