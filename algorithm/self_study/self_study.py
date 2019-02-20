import sys
sys.stdin = open('sample_input(6).txt', 'r')


T = int(input())
for test_case in range(1, 11):
    code = str(input().split())
    op = ['+', '-', '*', '/']
    stack = []
    for i in code:
        if i not in op:
            stack.append(i)
        elif len(stack) >= 2 and i in op:
            if i == '+':
                stack.append(int(stack[-2]) + int(stack[-1]))
                del stack[-3:-1]
            elif i == '-':
                stack.append(int(stack[-2]) - int(stack[-1]))
                del stack[-3:-1]
            elif i == '*':
                stack.append(int(stack[-2]) * int(stack[-1]))
                del stack[-3:-1]
            elif i == '/':
                stack.append(int(stack[-2]) / int(stack[-1]))
                del stack[-3:-1]
        elif i == '.':
            break
        else:
            result = 'error'
            break
    if len(stack) >= 2:
        result = 'error'
    else:
        result = stack[0]
    print(f'#{test_case} {result}')


