#Fibonacci
while True:
    ntermo = int(input("Quantos termos devo mostrar?"))

    # Primeiro dois termos 
    n1, n2 = 0, 1
    count = 0

    # olhe se o n° é verdadeiro
    if ntermo <= 0:
        print("Por favor, coloque um numero positivo")
    # Se tiver só um termo volte o n1
    elif ntermo == 1:
        print("A Sequencia de Fibonacci é", ntermo,":")
        print(n1)
    #gere a sequencia de fibonacci
    else:
        print("Fibonacci sequence:")
        while count < ntermo:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    
    print()  # linha em branco para melhor formatação