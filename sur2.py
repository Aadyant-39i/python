guess = input("Is " + str(n) + " a power of 4? (yes/no): ")
input("Check: n % 3 == 1.  Press Enter ")
is_pow4 = n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
if is_pow4:
    print(" ", n, " binary:", bin(n)[2:], " power of 4: yes   your guess:", guess)
else:
    print(" ", n, " binary:", bin(n)[2:], " power of 4: no    your guess:", guess)
