while True:
    a, op, b = input().split()
    if op == "?":
        break
    a, b = int(a), int(b)
    ans = 0
    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "*":
        ans = a * b
    elif op == "/":
        ans = a // b
    print(ans)
