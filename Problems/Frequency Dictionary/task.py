# put your python code here
string = input()
word_dict = {}
for word in string.split():
    if word.lower() in word_dict:
        word_dict[word.lower()] += 1
    else:
        word_dict[word.lower()] = 1
for keys, values in word_dict.items():
    print(keys, values)
