def _3_and_5_multiple(num):
    sum  = 0
    for i in range (num):
        if i%3 == 0 and i%5 == 0:
            sum+=i
            #print(sum)
            continue
        elif i%5 == 0:
            sum+=i
            #print(sum)
            continue
        elif i%3 == 0:
            sum+=i
            #print(sum)
            continue
        else:
            continue
    
    return sum


print(_3_and_5_multiple(10))
print(_3_and_5_multiple(1000))