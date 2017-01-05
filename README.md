Egyptinator README
============

About
-----
Egyptinator is an encryption program that is ultra mega yuge secure.

How it works
------------
**C1:** Random *KEY* Generated

**C2:** Alphabet Randomized with *KEY* (MD5)

**C3:** *MESSAGE* -> Monoalphabetic Cipher

**C4:** Polyalphabetic Cipher Generated With Current Date/Time (*KEY2*)

**C5:** *MESSAGE{C3}* -> Polyalphabetic Cipher

**C6:** *MESSAGE{C5}* -> Monoalphabetic Cipher

**C7:** *KEY2* -> Monoalphabetic Cipher

**C8:** *KEY2{C7}* Inserted At Random Position in *MESSAGE{C5}*

Future Features
---------------
* Random key selection (random order, random # char)
* SHA-III instead of MD5
* Enigma Polyalphabetic Cipher
