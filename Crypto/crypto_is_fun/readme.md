CTF Challenge Writeup: Crypto is Fun

Challenge Breakdown
The challenge consists of three encoded parts. To retrieve the flag, we need to decode each part step by step.

Part 1: ROT13 Encoding
furyyzngrf{Pelc10_

Solution:
ROT13 is a simple letter substitution cipher that shifts letters 13 places in the alphabet.

Decoding using ROT13:

shellmates{Cryp10_

Part 2: Base64 Encoding (Applied 3 Times)
VFZSV1psWnFUbmxsVVQwOQ==

Solution:
Base64 encoding is a common method of encoding binary data as text. Since it is applied three times, we need to decode it three times.


1st Base64 Decode:

TVRWZlZqTnllUT09

2nd Base64 Decode:

MTVfVjNyeQ==

3rd Base64 Decode:

15_V3ry

Part 3: Base6 and Hex Encoding

N3VuXzcwcl9IYWNrZXJzfQ==

Solution:
1. Convert Hex to ASCII:
   N3VuXzcwcl9IYWNrzXJzfQ==
2. Decode Base64:
   7un_70r_Hack3rz

Final Flag:
shellmates{Cryp10_15_V3ry7un_70r_Hack3rz}

Conclusion
This challenge required knowledge of multiple encoding techniques, including ROT13, Base64 (applied multiple times), hexadecimal, and Base6-like encoding. By carefully applying the appropriate decoding methods in sequence, we successfully recovered the flag.
