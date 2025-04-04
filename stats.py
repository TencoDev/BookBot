def count_words(file_content):
    word_list = file_content.split()
    word_count = len(word_list)
    return word_count

def count_letters(file_content):
    letter_count_dict = {}
    for letter in file_content:
        letter = letter.lower()
        if letter not in letter_count_dict:
            letter_count_dict[letter] = 1
        else:
            letter_count_dict[letter] = letter_count_dict.get(letter) + 1

    return letter_count_dict

def sort_dict(letter_count_dict):
    sorted_dict = dict(sorted(letter_count_dict.items(), key= lambda item: item[1], reverse=True))
    return sorted_dict
