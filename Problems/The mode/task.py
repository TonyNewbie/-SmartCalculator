from collections import Counter


some_data = input().split()
freq_counter = Counter(some_data)
print(freq_counter.most_common(1)[0][0])
