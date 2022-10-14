import random
res = set()
maxi = 0
mx = -float('inf')
choice = str(input('Введите: свои параметры массива или случайные параметры массива: '))
if choice == 'свои параметры массива':
    dim = int(input('Введите размерность массива А: '))
    A = []
    for _ in range(dim):
        variable = float(input('Введите элемент массива А: '))
        if variable % 1 == 0:
            variable = int(variable)
            A.append(variable)
        else:
            A.append(variable)
    for i in range(dim):
        if A[i] > mx:
            mx = A[i]
            maxi = i
    for j in range(maxi + 1, dim):
        A[j] = 0
    print(*A)
elif choice == 'случайные параметры массива':
    dim = random.randint(1, 100)
    A = []
    for _ in range(dim):
        variable = random.uniform(1,100)
        if variable % 1 == 0:
            variable = int(variable)
            A.append(variable)
        else:
            A.append(variable)
    for i in range(dim):
        if A[i] > mx:
            mx = A[i]
            maxi = i
    for j in range(maxi + 1, dim):
        A[j] = 0
    print(*A)
else:
    print('Произошла ошибка, введите: свои параметры массива или случайные параметры массива')