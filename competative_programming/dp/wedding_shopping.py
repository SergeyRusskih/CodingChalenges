def wedding_shopping(wardrobe, budget):
    return shop(wardrobe, 0, budget, [0][0])

def shop(wardrobe, wardrobe_id, money_left, memo):
    if money_left < 0:
        return -1

    if memo[wardrobe_id][money_left] != -1:
        return memo[wardrobe_id][money_left]

    if len(wardrobe) - 1 == wardrobe_id:
        return money_left

    max_value = -1
    for item in enumerate(wardrobe[wardrobe_id]):
        max_value = max(max_value, shop(wardrobe, wardrobe_id + 1, money_left, memo))

    memo[wardrobe_id][money_left] = max_value
    return max_value

    

def test_example():
    wardrobe = [
        [6, 4, 8],
        [5, 10],
        [1, 5, 3, 5]
    ]
    #assert wedding_shopping(wardrobe, 20) == 19