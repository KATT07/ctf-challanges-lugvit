User needs 3 files
1. Pic in github for enigma settings
2. decode-me.txt generated after giving input to script
3. after-solving.txt generated after giving input to script

Cryptography (med-hard)  - Scripted in python
encoding:
flag+salt -> enigma cipher -> base64 -> wingdings -> binary(utf8)
decoding:
binary(utf8) -> wingdings -> base64 -> enigma decipher
settings for enigma machine given using a image from https://www.101computing.net/enigma-machine-emulator/
(Ring Setting indicated using notch)
(Reflector type indicated by editing name on website)
(Rotor type I II I photoshopped in image)

Hint 1:
No hashing
Hint 2:
8 bits in binary means utf?
Hint 3:
big machine from ww2 used by germany for encoding information
