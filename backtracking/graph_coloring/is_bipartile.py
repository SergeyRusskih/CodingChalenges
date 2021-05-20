# todo: https://leetcode.com/problems/is-graph-bipartite/
def is_bipartile(graph):
    if len(graph) < 2:
        return False
    elif len(graph) == 2:
        return True

    colors = { }

    def get_color(i):
        neighbours = graph[i]

        next = None
        for neighbour in neighbours:
            if neighbour in colors:
                if next == None:
                    next = colors[neighbour]
                elif colors[neighbour] != next:
                    return -1

        if next == 0:
            return 1

        return 0

    visited = set()
    for i, value in enumerate(graph):
        if i not in colors:
            queue = [i]
            while queue:
                current = queue.pop(0)
                visited.add(current)
                colors[current] = get_color(current)
                if colors[current] == -1:
                    return False

                for neighbour in graph[current]:
                    if neighbour not in visited:
                        queue.append(neighbour)

    return True

def test_2():
    result = is_bipartile([[1,3],[0,2],[1,3],[0,2]])
    assert result

def test_1():
    result = is_bipartile([[1,2,3],[0,2],[0,1,3],[0,2]])
    assert not result