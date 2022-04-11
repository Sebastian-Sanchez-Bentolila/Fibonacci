#@Author: Sebastian Sanchez Bentolila https://github.com/Sebastian-Sanchez-Bentolila

#Fibonacci series


n1, n2 = 0, 1
print(n1, n2, end=" ")
while n2<1597:
    n1 += n2
    n2 += n1
    print(n1, n2, end=" ")