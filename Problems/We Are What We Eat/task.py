# the list "meals" is already defined
# your code here
total_kcal = 0
for record in meals:
    total_kcal += record['kcal']
print(total_kcal)
