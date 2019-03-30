def isPrime(num):
        fact = 2
        while fact * fact <=  num:
            if num % fact == 0:
                return False
            fact += 1
        return True


def nthPrimeNum(num):
    primeCounter = 0
    nums = 1
    while primeCounter != (num):
        nums += 1
        if isPrime(nums):
            primeCounter += 1
            print(nums , primeCounter)

    return nums


print(nthPrimeNum(10001))


