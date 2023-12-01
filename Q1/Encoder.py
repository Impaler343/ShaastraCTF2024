# s = "cvpbPGSarkg_gvzr_Vyy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ"
# s = "qhcoCTF"
# k = "picoCTF"
# z = "shaastraCTF"
c1 = "abcdefghijklmnopqrstuvwxyz"
c2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def rot(a, n):
#     if a in c1:
#         return c1[(c1.index(a) + n) % 26]
#     if a in c2:
#         return c2[(c2.index(a) + n) % 26]


# def simple_encode(s):
#     x = s[0]
#     for i in range(len(s) - 1):
#         x += rot(s[i], n(s[i + 1]))
#     x += s[-1]
#     return x


# for i in range(len(s)):
#     print(ord(s[i]) - ord(k[i]))
#     c1 *= -1

# f = simple_encode(z)
# print(f)

# for i in range(len(f)):
#     print(n(z[i]), ord(f[i]) - ord(z[i]))

ss = "sbuomkxkwwlifbcwjaotbsrsrkwuknfffx"
answer = "supercalifragilisticexpialidocious"

s = answer[0]

for i in range(len(answer) - 1):
    s += chr((26 + ord(answer[i + 1]) - ord(answer[i])) % 26 + 96)


print(s)


# def caesar_cipher_decrypt(ciphertext, shift):
#     result = ciphertext[0]

#     for i in range(len(ciphertext) - 1):
#         result += chr(((ord(ciphertext[i + 1]) - ord("a") - shift) % 26) + ord("a"))

#     return result


# reversed_finder = caesar_cipher_decrypt(finder, shift)
# print(reversed_finder)
# finder = s[0]

# for i in range(len(s)-1):
#     finder += chr((minus(s[i+1]) + minus(s[i]))%26 + 96)

# print(finder)
