from sample import hello


def test__foo():
    assert True


def test__hello():
    assert hello.hello() == "hello"
