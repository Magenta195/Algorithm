
from typing import List

def calculate(expr: str, left: str, right: str) -> int:
    return int(left) + int(right) if expr == '+' else int(left) - int(right)

def convert_base(string_num: str, init_base: int, dest_base: int) -> str:
    try:
        num = int(string_num, init_base)
        result = ''
        while num:
            result += str(num % dest_base)
            num //= dest_base
        return result[::-1] if result else '0'
    except:
        return 'invalid'

def is_target_expression(expression: str) -> bool:
    return expression[-1] == 'X'

def is_matched_base(base: int, expression: str) -> bool:
    left, expr, right, _, result = expression.split()
    left = convert_base(left, base, 10)
    right = convert_base(right, base, 10)
    result = convert_base(result, base, 10)
    
    if left == 'invalid' or right == 'invalid':
        return False
    if is_target_expression(expression) :
        return True
    if result == 'invalid':
        return False
        
    return calculate(expr, left, right) == int(result)

def find_bases(expressions: List[str]) -> List[int]:
    bases = []
    for base in range(2, 10):
        is_matched = True
        for expression in expressions:
            if not is_matched_base(base, expression):
                is_matched = False
                break
        if is_matched:
            bases.append(base)
    return bases

    
def correct_target_expression(bases: List[int], expression: str) -> str:
    left, expr, right, equal, _ = expression.split()
    answer_set = set()
    for base in bases:
        l = convert_base(left, base, 10) 
        r = convert_base(right, base, 10) 
        if l == 'invalid' or r == 'invalid' :
            continue
    
        res = calculate(expr, l, r)
        print(res, base)
        res = convert_base(str(res), 10, base)
        print(res)
        answer_set.add(res)
    print(answer_set)
    res = list(answer_set)[0] if len(answer_set) == 1 else '?'
    return ' '.join((left, expr, right, equal, res))

def correct_expressions(bases: List[int], expressions: List[str]) -> List[str]:
    result = []
    for expression in expressions :
        if not is_target_expression(expression):
            continue
        res = correct_target_expression(bases, expression)
        result.append(res)
    return result
        

def solution(expressions):
    bases = find_bases(expressions)
    answer = correct_expressions(bases, expressions)
    
    return answer