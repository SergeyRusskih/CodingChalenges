def urlify(string):
    return string.strip().replace(" ", "%20")

def test_from_example():
    assert urlify("Mr John Smith ") == "Mr%20John%20Smith"