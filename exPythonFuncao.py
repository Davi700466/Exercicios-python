"""
Exercício: Fábrica de Funções de Operações Matemáticas

Imagine que você está construindo uma calculadora. Porém, ao invés de 
implementar cada operação matemática (soma, subtração, multiplicação e divisão) 
diretamente, você decide criar uma "fábrica de funções". Esta fábrica, quando fornecida 
com o nome de uma operação, deve retornar uma função que realiza a operação desejada.

Instruções:

    - Escreva uma função chamada fábrica de operações que aceite uma 
    string: 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.
    
    - Dependendo do argumento fornecido, sua função deve retornar uma das 
    operações matemáticas. Por exemplo, se o argumento for 'soma', a função 
    retornada deve ser capaz de somar dois números.
    
    - Se a operação não for reconhecida, retorne uma função que 
    imprima "Operação não suportada.".
    
    
Desafio Extra:
Adapte a fábrica para aceitar operações com 
mais de dois números. Por exemplo, a operação de soma deve 
ser capaz de somar três, quatro ou mais números de uma só vez.

Dica: Utilize argumentos variáveis (*args) para essa adaptação.
"""

def fábrica_de_funcões(operação):
    
    def soma(*args):
        
        return sum(args)
    

    def subtração(*args):
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado
    

    def multiplicação(*args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado
    
    def divisão(*args):
        resultado = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Divisão por zero não é permitida")
            resultado /= num
        return resultado
    
    

    if operação == "soma":
        return soma
    
    elif operação == "subtração":
        return subtração
    
    elif operação == "multiplicação":
        return multiplicação
    
    elif operação == "divisão":
        return divisão
    
    else:
        def operação_não_suportada(*args):
            return "Operação não suportada."
        return operação_não_suportada


adicionar = fábrica_de_funcões("soma")
print (adicionar(5, 3, 2, 9, 4, 7))

subtrair = fábrica_de_funcões("subtração")
print (subtrair(10, 4, 2))

multiplicar = fábrica_de_funcões("multiplicação")
print (multiplicar(5, 3, 2,))

dividir = fábrica_de_funcões("divisão")
print (dividir(10, 5, 1))

