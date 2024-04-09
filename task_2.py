# task 2

def all_primes(start, end):

    list_primes = []
    for i in range(start, end):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list_primes.append(i)
    return list_primes


print(all_primes(1, 10))