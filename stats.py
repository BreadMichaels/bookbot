def word_count(words):
    word_list = words.split()
    num_words = 0
    for word in word_list:
        num_words += 1
    return f"Found {num_words} total words"

def ch_count(words):
    new_string = words.lower()
    new_dict = {}
    for i in new_string:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict

def sort_on(items):
    return items["num"]

def dict_sort(dictionary):
    dict_list = []
    for i in dictionary.items():
        new_dict = {"char": i[0], "num": i[1]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

