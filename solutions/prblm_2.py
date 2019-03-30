sdef fib(num):
    if num == 1:
        return 1
    elif num == 2 :
        return 2
    else:
        return fib(num-1) + fib(num-2) 


def sum_even_fib():
    i = 1
    sum = 0
    max = 4000000
    while(fib(i) < max ):
        if fib(i)%2 == 0:
            sum+=fib(i)
        i+=1

    return sum
        

print(sum_even_fib())
        
        


