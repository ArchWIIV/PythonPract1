import math
def One():
    x = int(input("X - "))
    y = int(input("Y - "))
    #long(m, 100)
    m = math.sqrt(x**5 - math.fabs(x)) - math.sqrt(y + math.cos(x)) - \
        math.sqrt((y**7 + x + 53) / (math.log(y) + x**5 - 2))
    print(m)

def Two():
    x = int(input("X - "))
    if x < 61:
        m = x**5 - math.cos(x)
        print(m)
    elif 61<= x < 118:
        m =79*x**4 + math.cos(x)
        print(m)
    elif 118<= x < 155:
        m =math.tan(math.fabs(x) + x**5) - math.log(math.sin(x)  + x/11)
        print(m)
    else:
        m = x**4 + x**7/93 + 14
        print(m)

def Three():
    n = int(input("n - "))
    m = 0
    k = 0
    for i in range(1,n+1):
        m += (60*i**5 +i*8 + 71)

    for i in range(1,n+1):
        k += (79*i**4 + math.e**i)
    f = n/37 - k/47
    print(f)

def Fact(n):
    if n == 0:
        return 4
    elif n == 1:
        return 6
    else:
        return math.fabs(Fact(n - 1) + math.tan(Fact(n - 1)))

while True:
    choose = int(input("Выбор варианта задания(1,2,3,4 exit - 5) - "))
    if choose == 1:
        One()
    elif choose == 2:
        Two()
    elif choose == 3:
        Three()
    elif choose == 4:
        print(Fact(int(input("n - "))))
    else:
        print ("Завершение работы")
        break
