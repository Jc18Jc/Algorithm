def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def solve(expression, idx, current_value):
    if idx == len(expression):
        return current_value
    
    if idx == 0:
        return solve(expression, idx + 1, int(expression[idx]))
    
    max_value = float('-inf')
    
    next_value = int(expression[idx + 1])
    result_without_parenthesis = calculate(current_value, next_value, expression[idx])
    max_value = max(max_value, solve(expression, idx + 2, result_without_parenthesis))
    
    if idx + 2 < len(expression):
        next_value = calculate(int(expression[idx + 1]), int(expression[idx + 3]), expression[idx + 2])
        result_with_parenthesis = calculate(current_value, next_value, expression[idx])
        max_value = max(max_value, solve(expression, idx + 4, result_with_parenthesis))
    
    return max_value

N = int(input())
expression = input().strip()

result = solve(expression, 0, 0)
print(result)