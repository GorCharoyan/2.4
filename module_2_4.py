numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print('primes:',primes)
print('not_primes:',not_primes)
