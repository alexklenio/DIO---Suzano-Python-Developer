
texto = input("Informe um esto: ").strip().upper()
VOGAIS  = "AEIOU"

for letra in texto:
    if letra in VOGAIS:
        print(letra, end="")
else: 
    print()