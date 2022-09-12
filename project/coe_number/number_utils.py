def is_prime_list(numbers):
    for num in numbers:
        if ( num > 1):
            for n in range(2, num):
                if num % n == 0:
                    return False
        else:
            return False
    return True
# True == Prime numbers
# False == Not Prime numbers