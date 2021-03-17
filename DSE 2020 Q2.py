import time

A = [9, 8, 14, 10, 5, 7, 6, 12, 13]
B = [False] *20
S = 5
N = 10

def FC1(S, N):
    for i in range(S, S+N):
        found = False
        for j in range(0, N-1):
            if A[j] == i:
                found = True
        if found == False:
            print(i)


def FC2(S, N):
    for i in range(S, S+N):
        B[i] = False
    for j in range(0, N-1):
        B[A[j]] = True
    for i in range(S, S+N):
        if B[i] == False:
            print(i)


def FC2updated(S, N):
    for i in range(0, N):
        B[i] = False
    for j in range(0, N-1):
        B[A[j]-S] = True
    for i in range(0, N-1):
        if B[i] == False:
            print(i+S)

def FC3(S, N):
    temp = 0
    for i in range(S, S+N):
        temp = temp + i
    sum = 0
    for i in range(0, N-1):
        sum = sum + A[i]
    print(temp - sum)

for count in range(4):
    stime = time.time()
    if count == 0: FC1(5, 10)
    if count == 1: FC2(5, 10)
    if count == 2: FC2updated(5, 10)
    if count == 3: FC3(5, 10)
    etime = time.time()
    print("Execution time = ", format(etime - stime, ".8f"), "second")