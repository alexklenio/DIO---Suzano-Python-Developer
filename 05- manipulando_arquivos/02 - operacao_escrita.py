arquivo = open("05- manipulando_arquivos/teste.txt", "w")


arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines([" escrevendo ", "um " , "novo " , "texto"])

arquivo.close()