# the list "walks" is already defined
# your code here
sum_distance = 0
for record in walks:
    sum_distance += record['distance']
print(int(sum_distance / len(walks)))
