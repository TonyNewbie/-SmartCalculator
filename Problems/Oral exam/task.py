from collections import deque
exam_queue = deque()
n = int(input())
for _ in range(n):
    input_value = input().split()
    if input_value[0] == 'READY':
        exam_queue.appendleft(input_value[1])
    elif input_value[0] == 'EXTRA':
        exam_queue.appendleft(exam_queue.pop())
    elif input_value[0] == 'PASSED':
        print(exam_queue.pop())
