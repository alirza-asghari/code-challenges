
def collatz_sequence(n, sequence=[]):
    if sequence is None:
        sequence = [n]
    if n == 1:
        return sequence
    if n % 2 == 0:
        next_number = int(n / 2)
    elif n % 2 != 0:
        next_number = n * 3 + 1
    sequence.append(next_number)
    return collatz_sequence(next_number, sequence)    

def max_collatz(n):
    collatz_seq = collatz_sequence(n)
    print(max(collatz_seq))

max_collatz(85)
