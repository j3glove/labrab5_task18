import random
import time
import numpy as np
def printmatrix(matrix):
    print("\n")
    for i in matrix:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

countneg=0
countpos=0
summ=0
        #пользовательский ввод
while True:    #Ввод числа N
    N = input("Введите число N без пробелов в диапазоне от 3 до 1000 включительно:    ")
    if N.isdigit():
        N=int(N)
        if N >= 3 and N <= 1000:
            break
        else:
            print("Вы ввели число не входящее в диапазон")
    else:
        print("Вы некорректно ввели число")


while True: #Ввод числа K
    minusflag = False
    K = input("Введите K число без пробелов   ")
    K=K.strip()
    if K[0]=="+" or K[0]=="-":
        if K[0]=="-":
            K = K.replace("-","")
            minusflag=True
        else:
            K = K.replace("+","")
    if K.isdigit():
        if minusflag == True:
            K = - int(K)
            break
        else:
            K=int(K)
            break
    else:
        print("Вы неккоректно ввели число")

A=[[0]*N for i in range(N)] # создание матрицы A
for i in range(N):
    for j in range(N):
        A[i][j] = random.randint(-10,10)
print("Матрица: A")
print(A)

F = [[0] * N for i in range(N)]  # Создание матрицы F равной A
for i in range(N):
    for j in range(N):
        F[i][j] = A[i][j]
print("Матрица: F")
print(F)

B = [[0]*int(N//2) for i in range(N//2)] # создание матрицы B
for i in range(int(len(A)//2)):
    for j in range(int((len(A))//2)):
        B[i][j]=A[i][j]

C = [[0]*int(N//2) for i in range(N//2)] # создание матрицы C
for i in range(int(len(A)//2)):
    for j in range(int((len(A)+1)//2),len(A)):
        C[i][j-int((N+1)/2)]=A[i][j]

E = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы E
for i in range((int(len(A)+1) // 2),len(A)):
    for j in range(int((len(A) + 1) // 2), len(A)):
        E[i - int((N+1)/2)][j - int((N + 1) / 2)] = A[i][j]

D = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы D
for i in range(int(len(A) // 2),len(A)):
    for j in range(int((len(A)) // 2)):
        D[i-int((N+1)/2)][j] = A[i][j]


G = [[0] * N for i in range(N)]  # Создание матрицы G
for i in range(N):
    for j in range(i+1):
        G[i][j] = A[i][j]
print("Матрица: G")
print(G)

det= np.linalg.det(np.array(A))  # определитель матрицы A
print("Определитель матрицы A: ",det)

Atransp=np.transpose(A) #транспонированная матрица A


Ainv=np.linalg.inv(A) # обратная матрица A
print(Ainv)



for i in range(N//2): # Счетчик положительных элементов в четных столбцах матрицы C
    for j in range(N//2):
        if j%2==0 and C[i][j]>0:
            countpos+=1




for i in range(N//2): # Счетчик отрицательных элементов в нечетных столбцах матрицы C
    for j in range(N//2):
        if j%2==1 and C[i][j] < 0:
            countneg+=1

if countpos > countneg: # При выполнении этого условия мы меняем С и B  местами симметрично
    for i in range(N//2):
        for j in range(N//2):
            temp=B[i][N//2-j-1]
            B[i][N//2-j-1]=C[i][j]
            C[i][j]=temp
    for i in range(N//2):
        for j in range(N//2):
            F[i][j]=B[i][j]
            F[i][(N+1)//2+j]=C[i][j]
else:                               # Иначе меняем C и E местами несимметрично
    for i in range(N//2):
        for j in range((N+1)//2,N):
            F[i][j]=E[i][j-N//2-N%2]
    for i in range((N+1)//2,N):
        for j in range((N+1)//2,N):
            F[i][j]=C[i-N//2-N%2][j-N//2-N%2]
print("Преобразованная Матрица F:")
print(F)

Ftransp=np.transpose(F)

for i in range(N):
    for j in range(N):
        if i == j:
            summ+=F[i][j]
        if i == N-j-1:
            summ+=F[i][j]
if N%2==1:
    summ-=F[N//2][N//2]

if det > summ:
    print(np.dot(np.array(A),(Atransp))-K*np.dot(F,Ainv))
else:
    print((K*Ainv+G-Ftransp)*K)



