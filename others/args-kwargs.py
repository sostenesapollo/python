"""
	*args 
	
	Usamos quando não sabemos quantos
	argumentos serão passados para uma
	função.

	*kwargs

	Não sabemos quantos argumentos de 
	palavra chave serão passados para uma
	função
"""

def argsKwargs(*a, **k):
	print(a)
	print(k)

argsKwargs('1', 1, 'site.com', upvote='yes', is_true=True, k=[1,2,3])
