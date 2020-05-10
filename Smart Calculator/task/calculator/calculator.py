from collections import deque


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def execute_command(command):
    if command == '/help':
        return ('The program calculates expressions containing +, -, *, /, ^ operations and parenthesis\n'
                'On this stage you also can use variables\n'
                'To see a list of variables type /vars command.')
    elif command == '/vars':
        variables_list = ''
        for key, value in variables.items():
            variables_list += f'{key} = {value}\n'
        return variables_list[:-1]
    elif command == '/exit':
        return -1
    else:
        return 'Unknown command'


def digits_in_string(string):
    digits = '0123456789'
    for char in string:
        if char in digits:
            return True
    return False


def assignment(string):
    global variables
    if string.count('=') > 1:
        print('Invalid assignment')
    else:
        left_side = string[:string.find('=')].strip()
        right_side = string[string.find('=') + 1:].strip()
        if digits_in_string(left_side):
            print('Invalid identifier')
        elif not is_int(right_side):
            if digits_in_string(right_side):
                print('Invalid assignment')
            else:
                try:
                    variables[left_side] = variables[right_side]
                except KeyError:
                    print('Unknown variable')
        else:
            variables[left_side] = int(right_side)
        return


def get_value(name):
    if is_int(name):
        return int(name)
    elif not digits_in_string(name):
        try:
            return variables[name]
        except KeyError:
            return 'Unknown variable'
    else:
        return 'Invalid identifier'


def check_sequences(expression):
    if '**' in expression or '//' in expression or '^^' in expression:
        return 'Invalid expression'
    while '--' in expression:
        expression = expression.replace('--', '+')
    while '++' in expression:
        expression = expression.replace('++', '+')
    while '+-' in expression or '-+' in expression:
        expression = expression.replace('+-', '-')
        expression = expression.replace('-+', '-')
    return expression


# leads expressions to a convenient form for calculations
# separates operations, operands and parenthesis
def expression_separation(expression):
    operations = ['(', ')', '+', '-', '*', '/', '^']
    normalized_expression = []
    part = ''
    for char in expression:
        if char in operations:
            if part.strip():
                normalized_expression.append(part.strip())
                part = ''
            normalized_expression.append(char)
        else:
            part += char
    if part:
        normalized_expression.append(part.strip())
    return normalized_expression


# checking for unary minus and replacing variables with their values
def variables_replacement(expression):
    operations = ['+', '-', '*', '/', '^', '(']
    changed_expression = []
    for i in range(len(expression)):
        if not (expression[i] in operations or expression[i] == ')'):
            expression[i] = str(get_value(expression[i]))
    start_index = 0
    if expression[0] == '-':
        changed_expression.append(expression[0] + str(expression[1]))
        start_index = 1
    for i in range(start_index, len(expression)):
        if expression[i] == '-' and expression[i - 1] in operations:
            changed_expression.append(expression[i] + str(expression[i + 1]))
        else:
            changed_expression.append(expression[i])
    return changed_expression


def infix_to_postfix(expression):
    priorities = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = deque()
    result = ''
    for part in expression:
        if is_int(part):
            result += part + ' '
        elif not stack or stack[-1] == '(' or part == '(':
            stack.append(part)
        elif part == ')':
            while stack[-1] != '(':
                result += stack.pop() + ' '
            stack.pop()
        elif priorities[stack[-1]] < priorities[part]:
            stack.append(part)
        elif priorities[stack[-1]] >= priorities[part]:
            while stack and (stack[-1] != '(' or priorities[stack[-1]] >= priorities[part]):
                result += stack.pop() + ' '
            stack.append(part)
    for _ in range(len(stack)):
        result += stack.pop() + ' '
    return result.split()


def evaluate(expression):
    operations = ['+', '-', '*', '/', '^']
    queue = deque()
    for part in expression:
        if part not in operations:
            queue.append(int(part))
        else:
            second_operand = queue.pop()
            first_operand = queue.pop()
            if part == '+':
                queue.append(first_operand + second_operand)
            elif part == '-':
                queue.append(first_operand - second_operand)
            elif part == '*':
                queue.append(first_operand * second_operand)
            elif part == '/':
                queue.append(first_operand // second_operand)
            elif part == '^':
                queue.append(pow(first_operand, second_operand))
    return queue[-1]


variables = {}
while True:
    entered_expression = input()
    if entered_expression.startswith('/'):
        command_result = execute_command(entered_expression)
        if command_result == -1:
            print('Bye!')
            break
        else:
            print(command_result)
    elif not entered_expression:
            continue
    elif '=' in entered_expression:
        assignment(entered_expression)
    else:
        check_result = check_sequences(entered_expression)
        if check_result == 'Invalid expression':
            print(check_result)
        else:
            expression_without_variables = variables_replacement(expression_separation(check_result))
            if 'Unknown variable' in expression_without_variables:
                print('Unknown variable')
            elif 'Invalid identifier' in expression_without_variables:
                print('Invalid identifier')
            else:
                try:
                    print(evaluate(infix_to_postfix(expression_without_variables)))
                except (ValueError, IndexError):
                    print('Invalid expression')
