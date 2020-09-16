def most_common_word(paragraph, banned):
    paragraph = paragraph.replace(".", "").replace(",", "").replace("!", "").replace("?", "").lower()
    banned_dict = set(banned)
    paragraph_dict = {}

    for _, value in enumerate(paragraph.split(" ")):
        value = value.strip()
        if value in banned_dict:
            continue
        if value in paragraph_dict:
            paragraph_dict[value] += 1
        else:
            paragraph_dict[value] = 1
            
    max_value = None
    max_key = None
    for _, (key, value) in enumerate(paragraph_dict.items()):
        if max_value == None:
            max_value = value
            max_key = key
            continue
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
    


def test_most_common_word():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    assert most_common_word(paragraph, banned) == "ball"