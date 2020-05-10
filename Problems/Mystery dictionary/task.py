# `random_dict` has been defined
# the input is in the variable `word`
# write the rest of the code here
if random_dict.setdefault(word, 0) == 0:
    print('Not in the dictionary')
else:
    print(random_dict[word])
