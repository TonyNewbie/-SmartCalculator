from collections import deque
queue = deque()
n = int(input())
for _ in range(n):
    input_value = input().split()
    if input_value[0] == 'ISSUE':
        queue.appendleft(input_value[1])
    elif input_value[0] == 'SOLVED':
        queue.pop()
for _ in range(len(queue)):
    print(queue.pop())
