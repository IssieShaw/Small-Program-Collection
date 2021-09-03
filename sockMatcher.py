#!/bin/python3

def pairing_algorithm(ar):
    one_sock = []
    num_pairs = 0

    for i in ar:
        if i in one_sock:
            one_sock.remove(i)
            num_pairs += 1
        else:
            one_sock.append(i)

    return num_pairs


def validation(msg, valid = False):
    while not valid:
        try:
            var = int(input(msg))
            valid = 1 + var
            return var
        except ValueError:
            print("Please enter an integer.")


ar = []

print("""Welcome to the sock matcher!
Please answer the questions with integers (whole numbers).
Assign each colour of a sock a number, for example Purple is 1. 
""")

n = validation("How many socks do you have?: ")

for i in range(n):
    sock_num = validation(f"\nSock {i+1}. Enter the number of the sock colour: ")
    ar.append(sock_num)

result = pairing_algorithm(ar)

print(f"\nYou have a total of {result} pairs of socks.")
