arr = [0, 1, 2, 3, 4, 5]
sum = 0
for n in arr:
    sum = sum + n
    if n == 3:
        arr.insert(n, 10)
    if sum > 15:
        break
print(sum)
