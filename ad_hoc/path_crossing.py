# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', 
# each representing moving one unit north, south, east, or west, respectively. 
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, 
# if at any time you are on a location you have previously visited. Return false otherwise.

# https://leetcode.com/problems/path-crossing/
def path_crossing(path):
    if len(path) < 2:
        return False

    x, y = 0, 0
    coordinates = set([(x,y)])

    for p in path:
        if p is 'N':
            y += 1
        elif p is 'E':
            x -= 1
        elif p is 'W':
            x += 1
        else:
            y -= 1

        if (x,y) in coordinates:
            return True
        else:
            coordinates.add((x,y))

    return False

def test_1():
    result = path_crossing("NESWW")
    assert result

def test_2():
    result = path_crossing("NWS")
    assert not result