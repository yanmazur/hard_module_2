n = int(input())
result = ''
for i in range(1,n):
    for j in range(1,n):
        if n % (i+j) == 0 and i < j:
            result += str(i) + str(j)
print(result)


