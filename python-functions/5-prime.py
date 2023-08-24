def is_prime(number):
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        return True
    else:
        return False
