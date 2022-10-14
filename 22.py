import random
res = set()
choice = str(input('Введите: свои параметры массива или случайные параметры массива: '))
if choice == 'свои параметры массива':
    dimA = int(input('Введите размерность массива А: '))
    A = []
    for _ in range(dimA):
        variable = int(input('Введите элемент массива А: '))
        A.append(variable)
    dimB = int(input('Введите размерность массива B: '))
    B = []
    for _ in range(dimB):
        variable = int(input('Введите элемент массива B: '))
        B.append(variable)
    for i in range(dimA):
        for j in range(dimB):
            if A[i] == B[j]:
                res.add(A[i])
    print('Элементы, совпадающие у массивов А и В: ', *res)
elif choice == 'случайные параметры массива':
    dimA = random.randint(1, 100)
    A = []
    for _ in range(dimA):
        variable = random.randint(1,100)
        A.append(variable)
    dimB = random.randint(1, 100)
    B = []
    for _ in range(dimB):
        variable = random.randint(1,100)
        B.append(variable)
    for i in range(dimA):
        for j in range(dimB):
            if A[i] == B[j]:
                res.add(A[i])
    print('Элементы, совпадающие у массивов А и В: ', *res)

else:
    print('Произошла ошибка, введите: свои параметры массива или случайные параметры массива')
