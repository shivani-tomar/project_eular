import math
def large_prime_fact(num):
    fact = 2
    while(fact * fact <= num):
        while num%fact == 0:
            num /= fact
        fact += 1
    if num > 1:
        return num
    return fact
print(large_prime_fact(13195))  

print(large_prime_fact(600851475143))