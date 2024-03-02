from itertools import combinations_with_replacement

def is_prime(number): # check if a number is prime or not
    if number == 4: return False
    for i in range(2, number//2):
        if number % i == 0: return False
    return True

def euclid_generator(number):
    combinations = [] # to store all the combinations 
    prime_list = []
    result = 1 

    if is_prime(number):
        print('this is a prime number!')
        return
    
    for item in range(2, number//2):
        if is_prime(item):
            prime_list.append(item)
    
    for i in range(2, len(prime_list)):
        combinations.append(list(combinations_with_replacement(prime_list, i)))
    for i in range(len(combinations)):
        for j in range(len(combinations[i])):
            for prime_number in combinations[i][j]:
                result *= prime_number
            if number == result:
                print(f'{combinations[i][j]}') 
                return
            result = 1


number = int(input('enter a number: '))
euclid_generator(number)

