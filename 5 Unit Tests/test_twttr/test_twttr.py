from twttr import shorten


def test_title():
    assert shorten("Anaconda") == "ncnd"


def test_numbers():
    assert shorten("October 5 2023") == "ctbr 5 2023"


def test_interpunction():
    assert shorten("Hello!! :-)") == "Hll!! :-)"
