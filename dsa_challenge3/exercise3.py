def valid_parenthese(text):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for char in text:
        if char in "[({":
            stack.append(char)
        elif char in ")}]":
            if len(stack) == 0 or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
print(valid_parenthese("{[()]}"))
print(valid_parenthese("([)"))
print(valid_parenthese("((()))"))
print(valid_parenthese("{[}"))