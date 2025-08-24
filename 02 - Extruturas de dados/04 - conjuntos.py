set('abacaxi')  #{'b', 'a', 'c', 'x', 'i'}

set(('palio', 'gol', 'celta', 'palio')) #{'gol', 'celta', 'palio'}

linguagens = {'python', 'java', 'python'} 

linguagens.add('C#')
print(linguagens)

linguagens.discard('java') #remove o iten, se o mesmo não tiver ele continua
linguagens.pop()
linguagens.remove() #remove o iten, se o mesmo não tiver ele retorna uma mensagem de erro

codigo = list(linguagens)
print(codigo[0])


print(codigo)