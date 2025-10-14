arquivo = open("05- manipulando_arquivos\lorem.txt", "r")

# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readlines())

arquivo.close()

try:
    with open("05- manipulando_arquivos\lorem.txt", "r") as arquivo:
        print("Trabalhando com o arquivo")

except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
