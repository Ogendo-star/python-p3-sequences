#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print("[]")
        return
    
    fib_sequence = [0, 1]
    
    if length == 1:
        print("[0]")
        return
    
    for _ in range(2, length):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    

    print(str(fib_sequence[:length]))

   