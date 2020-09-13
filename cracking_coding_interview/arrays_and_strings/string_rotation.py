def is_rotated(original, rotated):
    return (rotated + rotated).__contains__(original)

def test_is_rotated():
    assert is_rotated("waterbottle", "erbottlewat")