print ('Programa para ver numeros')

numero1 = int(input('\nDigite o numero 1: '))

numero2 = int(input('\nDigite o numero 2: '))

numero3 = float(input('\nDigite o numero 3: '))

print ('\n a)O produto do dobro do primeiro com a metade do segundo:\n')

print ("Resposta:", int(numero1 * 2 * numero2/2))

print ('\n b)A soma do triplo do primeiro com o terceiro:\n')

resultB = numero1 * 3 + numero3

if resultB%int(resultB)==0:

    print("Resposta: ", int(resultB))

else:

    print("Resposta: ", resultB)

print ('\n c)O terceiro elevado ao cubo:\n')

resultC = numero3 ** 3

if resultC%int(resultC)==0:

    print("Resposta: ", int(resultC))

else:

    print("Resposta: ", resultC)