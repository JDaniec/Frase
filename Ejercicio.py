print("---------------------------------")
print("-----------Voacales--------------")


n = input("Digite una frase: ")
vocales = "aeiouAEIOU"
a = 0
e = 0
i = 0
o = 0
u = 0

for l in n:
    if l in vocales:
        if l == "a" or l == "A":
            a = a + 1
        elif l == "e" or l == "E":
            e = e + 1
        elif l == "i" or l == "I":
            i = i + 1
        elif l == "o" or l == "O":
            o = o + 1
        elif l == "u" or l == "U":
            u = u + 1

print(f"En la frase hay " + str(a) + " veces la 'a'")
print(f"En la frase hay " + str(e) + " veces la 'e'")
print(f"En la frase hay " + str(i) +  " veces la 'i'")
print(f"En la frase hay " + str(o) + " veces la 'o'")
print(f"En la frase hay "  + str(u) + " veces la 'u'")

    
