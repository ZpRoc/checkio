# ---------------------------------------------------------------- #

# Caesar Cipher (encryptor)
#   Encrypt the text
#   (Cryptography, text, encode-Decode)

# ---------------------------------------------------------------- #

# This mission is the part of the set. Another one - Caesar cipher decriptor.

# Your mission is to encrypt a secret message (text only, without special 
# chars like "!", "&", "?" etc.) using Caesar cipher where each letter of 
# input text is replaced by another that stands at a fixed distance. For 
# example ("a b c", 3) == "d e f"

# Input: A secret message as a string (lowercase letters only and white spaces)
# Output: The same string, but encrypted
# Precondition: 0 < len(text) < 50, -26 < delta < 26


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def to_encrypt(text, delta):
    #replace this for solution
    return ''.join(chr((ord(c) + delta - 97) % 26 + 97) if c != ' ' else ' ' for c in text)


def to_encrypt_1(text, delta):
    #replace this for solution
    str_out = ''
    for ch in text:
        if ch.isalpha():
            n = (ord(ch)+delta)
            n = n if n <= ord('z') else n - ord('z') + ord('a') - 1
            n = n if n >= ord('a') else n - ord('a') + ord('z') + 1
            str_out += chr(n)
        elif ch.isspace():
            str_out += ' '
    return str_out


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")

