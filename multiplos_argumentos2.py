def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"A chave é {chave} e o valor é {valor}")
    print(type(kwargs))

minha_funcao(nome="gui", idade=18, pais="Brasil")