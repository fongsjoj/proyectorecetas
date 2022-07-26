#Para que se graben los registros y se haga salto de linea. Se debe colocar al final del
#registro '\n' indicando un salto de linea
archivo = open('prueba1.txt', 'w')

#archivo.write('primer nuevo registro\n')

#archivo.write('ahora otro registro')
#ahora si sale
#primer nuevo registro
#ahora otro registro
#otra forma es colocar
archivo.write('''primer nuevo registro
segundo registro
tercer registro''')

archivo.close()