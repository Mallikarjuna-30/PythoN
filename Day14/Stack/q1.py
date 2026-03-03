# Paranthesis Matching
# Need to check wheather my expression is balanced or not

def isBalanced(exp):
    stack =[]
    for ch in exp:
        if ch in "[({":
            stack.append(ch)
        
        elif ch in ")}]":
            if stack ==[]:
                return False
        
            top = stack.pop()
        
        if (ch == ')' and top != '(') or (ch =='}' and top != '{') or (ch == '[' and top != ']'):
            return False
    
    return len(stack) == 0

print(isBalanced('{({})}'))
print(isBalanced('{({}'))