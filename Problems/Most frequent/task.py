from collections import Counter
text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")
freq_dict = Counter(text.split())
n = int(input())
most_common = freq_dict.most_common(n)
for word in most_common:
    print(word[0], word[1])
