
import base64
import sys

st = sys.argv[1]

print("Original Flag")
print(st)

# Enigma Encoder - www.101computing.net/enigma-encoder/

# ----------------- Enigma Settings -----------------
rotors = ("I", "II", "I")
reflector = "UKW-B"
ringSettings = "APA"
ringPositions = "ZOB"
plugboard = "LU GV IT"


# ---------------------------------------------------

def caesarShift(str, amount):
    output = ""

    for i in range(0, len(str)):
        c = str[i]
        code = ord(c)
        if ((code >= 65) and (code <= 90)):
            c = chr(((code - 65 + amount) % 26) + 65)
        output = output + c

    return output


def encode(plaintext):
    global rotors, reflector, ringSettings, ringPositions, plugboard
    # Enigma Rotors and reflectors
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor1Notch = "Q"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor2Notch = "E"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotor3Notch = "V"
    rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    rotor4Notch = "J"
    rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
    rotor5Notch = "Z"

    rotorDict = {"I": rotor1, "II": rotor2, "III": rotor3, "IV": rotor4, "V": rotor5}
    rotorNotchDict = {"I": rotor1Notch, "II": rotor2Notch, "III": rotor3Notch, "IV": rotor4Notch, "V": rotor5Notch}

    reflectorB = {"A": "Y", "Y": "A", "B": "R", "R": "B", "C": "U", "U": "C", "D": "H", "H": "D", "E": "Q", "Q": "E",
                  "F": "S", "S": "F", "G": "L", "L": "G", "I": "P", "P": "I", "J": "X", "X": "J", "K": "N", "N": "K",
                  "M": "O", "O": "M", "T": "Z", "Z": "T", "V": "W", "W": "V"}
    reflectorC = {"A": "F", "F": "A", "B": "V", "V": "B", "C": "P", "P": "C", "D": "J", "J": "D", "E": "I", "I": "E",
                  "G": "O", "O": "G", "H": "Y", "Y": "H", "K": "R", "R": "K", "L": "Z", "Z": "L", "M": "X", "X": "M",
                  "N": "W", "W": "N", "Q": "T", "T": "Q", "S": "U", "U": "S"}

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotorANotch = False
    rotorBNotch = False
    rotorCNotch = False

    if reflector == "UKW-B":
        reflectorDict = reflectorB
    else:
        reflectorDict = reflectorC

    # A = Left,  B = Mid,  C=Right
    rotorA = rotorDict[rotors[0]]
    rotorB = rotorDict[rotors[1]]
    rotorC = rotorDict[rotors[2]]
    rotorANotch = rotorNotchDict[rotors[0]]
    rotorBNotch = rotorNotchDict[rotors[1]]
    rotorCNotch = rotorNotchDict[rotors[2]]

    rotorALetter = ringPositions[0]
    rotorBLetter = ringPositions[1]
    rotorCLetter = ringPositions[2]

    rotorASetting = ringSettings[0]
    offsetASetting = alphabet.index(rotorASetting)
    rotorBSetting = ringSettings[1]
    offsetBSetting = alphabet.index(rotorBSetting)
    rotorCSetting = ringSettings[2]
    offsetCSetting = alphabet.index(rotorCSetting)

    rotorA = caesarShift(rotorA, offsetASetting)
    rotorB = caesarShift(rotorB, offsetBSetting)
    rotorC = caesarShift(rotorC, offsetCSetting)

    if offsetASetting > 0:
        rotorA = rotorA[26 - offsetASetting:] + rotorA[0:26 - offsetASetting]
    if offsetBSetting > 0:
        rotorB = rotorB[26 - offsetBSetting:] + rotorB[0:26 - offsetBSetting]
    if offsetCSetting > 0:
        rotorC = rotorC[26 - offsetCSetting:] + rotorC[0:26 - offsetCSetting]

    ciphertext = ""

    # Converplugboard settings into a dictionary
    plugboardConnections = plugboard.upper().split(" ")
    plugboardDict = {}
    for pair in plugboardConnections:
        if len(pair) == 2:
            plugboardDict[pair[0]] = pair[1]
            plugboardDict[pair[1]] = pair[0]

    plaintext = plaintext.upper()
    for letter in plaintext:
        encryptedLetter = letter

        if letter in alphabet:
            # Rotate Rotors - This happens as soon as a key is pressed, before encrypting the letter!
            rotorTrigger = False
            # Third rotor rotates by 1 for every key being pressed
            if rotorCLetter == rotorCNotch:
                rotorTrigger = True
            rotorCLetter = alphabet[(alphabet.index(rotorCLetter) + 1) % 26]
            # Check if rotorB needs to rotate
            if rotorTrigger:
                rotorTrigger = False
                if rotorBLetter == rotorBNotch:
                    rotorTrigger = True
                rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]

                # Check if rotorA needs to rotate
                if (rotorTrigger):
                    rotorTrigger = False
                    rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]

            else:
                # Check for double step sequence!
                if rotorBLetter == rotorBNotch:
                    rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
                    rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]

            # Implement plugboard encryption!
            if letter in plugboardDict.keys():
                if plugboardDict[letter] != "":
                    encryptedLetter = plugboardDict[letter]

            # Rotors & Reflector Encryption
            offsetA = alphabet.index(rotorALetter)
            offsetB = alphabet.index(rotorBLetter)
            offsetC = alphabet.index(rotorCLetter)

            # Wheel 3 Encryption
            pos = alphabet.index(encryptedLetter)
            let = rotorC[(pos + offsetC) % 26]
            pos = alphabet.index(let)
            encryptedLetter = alphabet[(pos - offsetC + 26) % 26]

            # Wheel 2 Encryption
            pos = alphabet.index(encryptedLetter)
            let = rotorB[(pos + offsetB) % 26]
            pos = alphabet.index(let)
            encryptedLetter = alphabet[(pos - offsetB + 26) % 26]

            # Wheel 1 Encryption
            pos = alphabet.index(encryptedLetter)
            let = rotorA[(pos + offsetA) % 26]
            pos = alphabet.index(let)
            encryptedLetter = alphabet[(pos - offsetA + 26) % 26]

            # Reflector encryption!
            if encryptedLetter in reflectorDict.keys():
                if reflectorDict[encryptedLetter] != "":
                    encryptedLetter = reflectorDict[encryptedLetter]

            # Back through the rotors
            # Wheel 1 Encryption
            pos = alphabet.index(encryptedLetter)
            let = alphabet[(pos + offsetA) % 26]
            pos = rotorA.index(let)
            encryptedLetter = alphabet[(pos - offsetA + 26) % 26]

            # Wheel 2 Encryption
            pos = alphabet.index(encryptedLetter)
            let = alphabet[(pos + offsetB) % 26]
            pos = rotorB.index(let)
            encryptedLetter = alphabet[(pos - offsetB + 26) % 26]

            # Wheel 3 Encryption
            pos = alphabet.index(encryptedLetter)
            let = alphabet[(pos + offsetC) % 26]
            pos = rotorC.index(let)
            encryptedLetter = alphabet[(pos - offsetC + 26) % 26]

            # Implement plugboard encryption!
            if encryptedLetter in plugboardDict.keys():
                if plugboardDict[encryptedLetter] != "":
                    encryptedLetter = plugboardDict[encryptedLetter]

        ciphertext = ciphertext + encryptedLetter

    return ciphertext


# Main Program Starts Here
plaintext = st
ciphertext = encode(plaintext)
print("Enigma text: " + ciphertext)

sample_string = ciphertext.lower()
sample_string_bytes = sample_string.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Base64 string: {base64_string}")

print("  ##### Wingding #####")

encrypted = base64_string
sub = {
    'a': '♋︎', 'b': '♌︎', 'c': '♍︎',
    'd': '♎︎', 'e': '♏︎', 'f': '♐︎',
    'g': '♑︎', 'h': '♒︎', 'i': '♓︎',
    'j': '🙰', 'k': '🙵', 'l': '●︎',
    'm': '❍︎', 'n': '■︎', 'o': '□︎',
    'p': '◻︎', 'q': '❑︎', 'r': '❒︎',
    's': '⬧︎', 't': '⧫︎', 'u': '◆︎',
    'v': '❖︎', 'w': '⬥︎', 'x': '⌧︎',
    'y': '⍓︎', 'z': '⌘︎',
    'A': '✌', 'B': '👌', 'C': '👍',
    'D': '👎', 'E': '☜', 'F': '☞',
    'G': '☝', 'H': '☟', 'I': '✋',
    'J': '☺', 'K': '😐', 'L': '☹',
    'M': '💣', 'N': '☠', 'O': '⚐',
    'P': '🏱', 'Q': '✈', 'R': '☼',
    'S': '💧', 'T': '❄', 'U': '🕆',
    'V': '✞', 'W': '🕈︎', 'X': '✠',
    'Y': '✡', 'Z': '☪',
    ' ': ' ', ',': ',', '.': '.',
    '"': '"', "'": "'", '-': '-',
    '?': '✍︎', '!': '✏︎', ';': ';',
    ':': ':', '(': '(', ')': ')',
    '’': '’', '—': '—', '“': '“',
    '”': '”','0':'📁︎','_':'♉︎','=':'🖬︎',
    '1':'📂','2':'📄','3':'3',
    '4':'4','5':'5','6':'⌛',
    '7':'7','8':'8','9':'9'
}
decrypt = ''
for letter in encrypted:
    decrypt = decrypt + sub[letter]
print(decrypt)

print("  ##### Bytes #####")

a_string = decrypt

a_byte_array = bytearray(a_string, "utf8")
byte_list = []

for byte in a_byte_array:
    binary_representation = bin(byte)
    byte_list.append(binary_representation)

b_strr=""
for i in byte_list:
    b_strr+=i[2::]+" "
print(byte_list)
print(b_strr)

# Save to challange file

f=open("/app/decode-me.txt","w")
f.write(b_strr)
f.close()


#CHANGED AFTER LEARNING FLAG IS NOT CASE-SENSITIVE UNCOMMENT IF FLAG IS CASE SENSITIVE
#lst=[]
#for i in range(len(st)):
#    if st[i].isupper():
#            lst.append(str(i))
#f=open("/app/after-solving.txt","w")
#f.write("Change Following indices to uppercase before submitting flag \n")
#for i in lst:
#    f.write(i+" ")
#f.write("\nindices start from 0,1,2...")
#f.close()
