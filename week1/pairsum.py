num = [1,2,3,4,5,6,7,8,9,10]
result = []
target = int(input("Enter a target value: "))

for i in range(len(num)):
    for j in range(i+1, len(num)):
        print(num[i], num[j])
        if num[i] + num[j] == target:
            result.append((num[i], num[j]))

print(result)