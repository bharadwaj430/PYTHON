#find the prime numbers for the given range---100
begin_num = int(input("Enter begin_num: "))
end_num = int(input("Enter end_num: "))

primes = [n for n in range(begin_num, end_num+1) if n > 1 and all(n % i != 0 for i in range(2, n))]

print(primes)






