import random

print('Juego de la mazmorra\n'
      '--------------------\n'
      '\n'
      'Tú y tu compañero de celda os acabáis de escapar de la prisión espacial, habéis burlado a los guardias y os \n'
      'dirigís hacia el exterior. Entrais en una mazmorra controlada por mounstros alienigenas, uno de los guardias \n'
      'ataca a tu compañero, se lo lleva pero tu pasas desapercibido escondido en las sombras. El guardia se retira, \n'
      'es tu posibilidad de escapar. Hacia donde te diriges?\n'
      '\n'
      'A la izquieda tienes una puerta semiabierta, a la derecha una escotilla en el suelo.')

opcion = input('[OPCION (A) - Puerta semiabierta] | [OPCION (B) - Escotilla en el suelo]: ')

if opcion == 'A': #puerta semiabierta
      print('Entras en la puerta semiabierta y otro guardia te descubre, qué haces?')
      opcion = input('[OPCION (A) - Te haces el dormido] | [OPCION (B) - Sales corriendo hacia la siguiente puerta]: ')

      if opcion == 'A': #final malo_#1
            print('El guardia te atrapa. Te encierran en una celda de máxima seguridad\n'
                  'Fin.')
            exit()
      elif opcion == 'B': #pincho_si_o_no
            print('Después de esa puerta encuentras una rana mutante que te regala un puñal casero hecho con la pata de '
                  'una mesa, lo aceptas? ')
            opcion = input('[OPCION (A) - Sí] | [OPCION (B) - No]: ')

            if opcion == 'A': #pincho_si
               print('Coges el pincho y avanzas, hay dos pasillos circulares, no ves el final de ninguno de los dos, uno'
                     ' está a la derecha y el otro a la izquierda, cual tomas?')

               opcion = input('[OPCION (A) - Izquierda] | [OPCION (B) - Derecha]: ')

               if opcion == 'A': #Izquierda_final_malo_#2
                     print('La habitación se hace cada vez más oscura, ves tan poco que caes en un agujero en el suelo con'
                       ' pinchos, mueres a las 2 horas de forma lenta y dolorosa.\n'
                       'Fin.')
                     exit()
               elif opcion == 'B':#Derecha_final_bueno_#1
                     print('Encuentras la salida. En la puerta hay aparcado un Ferrari espacial, te montas, es tu día de '
                         'suerte, las llaves están puestas. Huyes hacia el horizonte.\n'
                         'Has ganado!!!!\n'
                         'Fin.')
                     exit()
            elif opcion == 'B':#pincho_no_final_malo_#3
                  print('La rana te devora, mueres de forma rápida, el veneno hace efecto casi de manera instantanea.\n'
                        'Fin.')
                  exit()
elif opcion == 'B': #escotilla_en_el_suelo
      print('Caes en una zona inundada, el agua te llega hasta las rodillas, avanzas durante media hora y finalmente '
            'llegas a una zona abierta, seca y con luz, parecen unas alcantarillas.\n'
            'Ahí encuentras un palo largo, parece algo pesado, pero podría servir, lo coges?')
      opcion = input('[OPCION (A) - Sí] | [OPCION (B) - No]: ')

      palo_en_inventario = False

      if opcion == 'A':
            print('Coges el palo')
            palo_en_inventario = True
      elif opcion == 'B':
            print('No coges el palo')
      else: #final_malo_#4
            print('No has elegido ningúna opción valida. Mueres!')
            exit()

      numero_random_rata = random.randint (1,100)

      print('Sigues adelante, encuentras una rata de 2 metros, la rata te pregunta cuanto es 13 * {}.'.format(
            numero_random_rata))
      opcion = int(input('Cúal es el resultado? '))

      if opcion == 13 * numero_random_rata: #final_malo_#5
            print('La rata te asesina no soporta a los cerebritos.\n'
                  'Fin.')
      else:
            print('La rata abre una puerta delante de ti, parece un pasillo que lleva hasta la salida. Lo recorres, '
                  'llegas al final, el tunel se derrumba detras de ti, no hay salida más que una especie de boca de '
                  'alcantarilla,\n'
                  'pero esta lejos de tu alcance. Qué haces?')
            opcion = input('[OPCION (A) - Esperas a que alguien te rescate] | [OPCION (B) - Intentas salir] ')

            if opcion == 'A': #final_malo_#6
                  print('Un montón de ratas aparecen y te devoran vivo. Es tu fin.\n'
                        'Fin.')
                  exit()
            elif opcion == 'B' and palo_en_inventario: #final_bueno_#2
                  print('Usas el palo que cogiste antes para impulsarte, consigues trepar y salir del laberinto. En la'
                        ' puerta hay aparcado un Ferrari espacial, te montas, es tu día de suerte, las llaves están puestas.\n'
                        'Huyes hacia el horizonte.\n'
                        'Has ganado!!!!\n'
                        'Fin.')
                  exit()
            elif opcion == 'B' and palo_en_inventario == False: #final_malo_#7
                  print('No tienes como subir, si solo tuvieras un palo. Pero no lo tienes verdad? Así que finalmente te'
                        ' quedas atrapado.'
                        '\n'
                        '\n'
                        'Pasado un rato un montón de ratas aparecen y te devoran vivo, es tu fin.\n'
                        'Fin.')
                  exit()
            else: #final_malo_#8
                  print('No has elegido ningúna opción valida. Mueres!')
                  exit()
else: #estas_algarete
      print('No has elegido ningúna opción valida. Mueres!')
      exit()