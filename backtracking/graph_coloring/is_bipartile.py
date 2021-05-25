# https://leetcode.com/problems/is-graph-bipartite/
def is_bipartile(graph):
    if len(graph) < 2:
        return False
    elif len(graph) == 2:
        return True

    colors = { }
    def dfs(i, color):
        colors[i] = color
        for j in graph[i]:
            if j in colors:
                if colors[j] == color: return False
            else:
                if not dfs(j, 1 - color): return False

        return True

    for i in range(len(graph)):
        if i in colors: continue
        if not dfs(i, 0): return False

    return True

def test_2():
    result = is_bipartile([[1,3],[0,2],[1,3],[0,2]])
    assert result

def test_1():
    result = is_bipartile([[1,2,3],[0,2],[0,1,3],[0,2]])
    assert not result