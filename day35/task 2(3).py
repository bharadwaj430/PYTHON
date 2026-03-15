# *args-if we don't know how many no.of parameters will be pass by the user
def find_primes(*args):
    start = args[0]
    end = args[1]
    primes = [n for n in range(start, end+1) if n > 1 and all(n % i != 0 for i in range(2, n))]
    return primes

result = find_primes(1, 100)
print(result)