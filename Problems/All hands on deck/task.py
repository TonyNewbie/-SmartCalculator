card_rank = {'2': 2, '3': 3, '4': 4, '5': 5,
             '6': 6, '7': 7, '8': 8, '9': 9,
             '10': 10, 'Jack': 11, 'Queen': 12,
             'King': 13, 'Ace': 14}
average = 0
for _ in range(6):
    card = input()
    average += card_rank[card]
print(average / 6)
