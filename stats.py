def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_characters(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})


    sorted_list.sort(key=lambda x: x["num"], reverse=True)

    return sorted_list
