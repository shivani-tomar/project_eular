def sum_of_squares(n):
    return (n *(n+1)*((2*n)+1))/6


def square_of_sums(n):
    return ((n*(n+1))/2)**2


def difference(n):
    return square_of_sums(n) - sum_of_squares(n)


print(difference(100))

    


