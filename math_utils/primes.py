from math import ceil, sqrt


def isprime(x):
    """
    Simple function to check if integer is prime.
    """
    square_root = ceil(sqrt(x))

    if square_root < 2:
        return False

    if x == 2:
        return True

    if square_root == 2:
        square_root += 1

    for i in range(2, square_root):
        remainder = x % i
        
        if remainder == 0:
            return False

    return True



    
