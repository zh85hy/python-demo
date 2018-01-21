# coding: utf-8


def count_words():
    words_dict = {}
    with open('words.txt', 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
    # for k, v in words_dict.items():
    #     print(k, v)
    result = sorted(words_dict.items(), key=lambda k: k[1], reverse=True)
    for k, v in result:
        print(k, v)


count_words()
