N = int(input())
table = list(map(int, input().split()))
table.reverse()

print(" ".join(map(str, table)))
