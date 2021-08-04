# https://leetcode.com/problems/task-scheduler/solution/
def task_scheduler(taks, n):
    frequencies = [0] * 26
    for task in tasks:
        frequencies[ord(task) - ord("A")] += 1
        
    frequencies.sort()
    f_max = frequencies.pop()
    idle_time = (f_max - 1) * n
        
    while frequencies and idle_time > 0:
        idle_time -= min(f_max - 1, frequencies.pop())

    return len(tasks) + max(0, idle_time)


def test_1():
    result = task_scheduler(["A","A","A","B","B","B"], 2)
    assert result == 8

def test_2():
    result = task_scheduler(["A","A","A","B","B","B"], 0)
    assert result == 6


def test_3():
    result = task_scheduler(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)
    assert result == 16