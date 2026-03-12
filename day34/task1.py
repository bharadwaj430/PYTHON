def fun():   # syntax
    print("Hello")

# print(fun())
fun()
def fun(name):
    return "hello " + name

n = input()
print(fun(n))
def add(a, b):
    print(a + b)

m, n = map(int, input().split())
add(m, n)
#factorial of a given number
def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)

n = int(input())
print(f(n))


#fibonacci series
#n = 5
#0,1,1,2,3

def fib(m):
    if m == 0 :
        return 0
    if m==1:
        return 1
    else :

        return fib(m-1)+fib(m-2)

n=int(input())
for i in range(n):
    print(fib(i),end="")



