MultiRSA refers to a modulus n from RSA encryption with multiple prime factors.

n is composed of 3 relatively small prime numbers (~30bit number to fit the flag and to make it factorable with our machines with a little bit of patience) and a big one (~480bit number ;) ).

n = p1^10 * p2^9 * p3^29 * P4

The 3 small prime numbers are raised to a power to make MultiRSA more challenging, especially the φ(n) which is necessary to calculate the exponent d.

φ(n) = (p1 - 1)*p1^9 * (p2 - 1)*p2^8 * (p3 - 1)*p3^28 * (P4 - 1)

Finally, the obtained message (number) can be converted to hexadecimal, then to ASCII to retrieve the flag !

m = 0x7368656c6c6d617465737b69735f69375f6d30725f3633637572333f7d

flag: shellmates{is_i7_m0r_63cur3?}