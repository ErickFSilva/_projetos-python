# Função print()

"""
Utilizada para exibir conteúdos em tela;
Ela recebe argumentos;
Os argumentos são separados por vírgula;
Por padrão, é adicionado um espaço entre a exibição de um argumento e outro. (São os argumentos não nomeados);
O argumento sep='' ou sep="" é utilizado para remover esses espaços impressos;
O argumento end='' ou end="" é utilizado no último argumento do 'print()';
Para quebrar a linha utiliza-se '\n' dentro de aspas simples ou duplas;
"""

# Argumentos não nomeados:
print('- Argumentos não nomados:')
print(12, 34)
print(56,78,'\n')

# Argumentos nomeados: 'sep' = separador
print("- Argumentos nomeados:")
print(12, 34, sep="-")
print(56, 78, sep=', ')
print(90, 12, sep="")
print('abc', end=" <-\n-> ")
print('def')