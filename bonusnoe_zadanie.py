dim = int(input('Введите размерность массива: '))
A = []
for _ in range(dim):
    variable = int(input('Введите элемент массива: '))
    A.append(variable)
delta = int(input('Введите значение delta: '))
mn = float('inf')
for i in range(dim):
    if A[i] < mn:
        mn = A[i]
count = 0
for i in range(dim):
    if A[i] - delta == mn:
        count += 1
print(count)
