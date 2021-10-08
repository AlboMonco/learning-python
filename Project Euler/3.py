import math
import time
def prime(number:int):
    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True 

def prime_factors(number:int):
    factors = []
    if prime(number):
        factors.append(number)
    else:
        for i in range(2,int(number/2 +1)):
            if number%i == 0 and prime(i):
                factors.append(i)
    return factors

def largest_prime_factor(number:int):
    return prime_factors(number)[-1]
    
def factorizer(number:int):
    list_primes_counted = count_primes(number)
    dict = {}
    for element in list_primes_counted:
        if element not in dict:
            dict[element] = 1
        else:
            dict[element] +=1
    return dict

def count_primes(number:int):
    list_prime = prime_factors(number)
    list_primes_counted = []
    for element in list_prime:
        while number%element == 0:
            number //= element
            list_primes_counted.append(element)
    return list_primes_counted
        

if __name__ == "__main__":
    start_time = time.time()
    print(factorizer(24))
    print("--- %s seconds ---" % (time.time() - start_time))

    