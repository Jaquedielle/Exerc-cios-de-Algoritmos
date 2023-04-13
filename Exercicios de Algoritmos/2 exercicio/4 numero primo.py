número = int(input ('Digite um número:'))
cont = 0
for x in range (2, número):
    if número % x == 0:
        cont = cont + 1 
        break
if cont == 0:
    print ('%d é primo ' % número)
else: 
    print ('%d nao é primo' % número) 
