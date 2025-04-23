
inserir_operador = input("+, -, *, / : ")

primeiro_numero = int(input("primeiro numero: "))

segundo_numero = int(input("segundo numero: "))


if inserir_operador == "+":
    resultado = primeiro_numero + segundo_numero
    print(resultado)

elif inserir_operador == "-":
    resultado = primeiro_numero - segundo_numero
    print(resultado)

elif inserir_operador == "*":
    resultado = primeiro_numero * segundo_numero
    print(resultado)

elif inserir_operador == "/":
    resultado = primeiro_numero / segundo_numero
    print(resultado)


