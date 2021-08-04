# bucket sort assumes that the input is generated
# by a random process that distributes elements uniformly and independently over
# the interval [0; 1)
def bucket_sort(arr, k): 
    buckets = [0] * (k + 1)
    for i in range(k + 1):
        buckets[i] = []

    for item in arr:
        buckets[item].append(item)

    result = []
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            result.append(buckets[i][j])

    return result