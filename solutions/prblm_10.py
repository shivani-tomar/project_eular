def isPrime(num):
        fact = 2
        while fact * fact <=  num:
            if num % fact == 0:
                return False
            fact += 1
        return True

def summation_of_prime(limit):
    sum = 0 
    for i in range(2, limit+1):
        if isPrime(i):
            sum += i
    return sum


print(summation_of_prime(2000000))