def check_parentheses(expression: str) -> bool:

    count1 = 0
    for par in expression:
        if par == "(":
            count1+=1
        if par == ")":
            count1-=1
        if count1 < 0:
            return False
    if count1 == 0:
        return True
    if count1 < 0 or count1 > 0:
        return False
    
print(check_parentheses("()(()))"))