import random

#prueba_usuario
bienvenida = 'Bienvenidos a mi juego espacial'
print('\n' + bienvenida + '\n' + '\n' + len(bienvenida) * "_" + '\n')
print('Todo lo que tienes que hacer para ganar es escapar. Entendido?\n')

entendido = input('[OPCION (A) - Sí] | [OPCION (B) - No]: ')

if entendido in ['A', 'Sí', 'Si', 'si', 'sí']:
    print('\nMuy bien, comencemos!')
elif entendido in ['B', 'NO', 'no']:
    print('\nOh, qué le vamos hacer?')
    exit()
else:
    print('No has elegido ningúna opción valida. Chao!')
    exit()

opcion_valida = False
intentos = 0
while not opcion_valida:

    #comienzo_del_juego
    print('\n Estas encerrado en un cuarto frío y oscuro. Solo tienes contigo unas baterías "AA" y un Walkie Talkie.\n'
      'No sabes que esta sucediendo.\n'
      'Esta es tu primera desición: \n')

    opcion = input('[OPCION (A) - Ponerle las baterías al Walkie Talkie] | [OPCION (B) - No ponerle las baterías al Walkie Talkie]: ')

    if opcion == 'A': #continuación_de_la_historia
        persona_extrana = 'Persona extraña: '
        tu = 'Tú: '
        print('\n Has decidio ponerle las baterías al Walkie Talkie. Este ejecicio sería bastante sencillo en cualquier otra\n'
          'situación, pero ahora implica un reto. El miedo, la incertidumbre y la falta de luz son grandes obstaculos.\n'
          'Aún así, sales victorioso.\n'
          '\n'
          'No hay tiempo para celebrar. Se comienza a escuchar una voz por el aparato. Está pidiendo ayuda.')
        opcion_valida = True
        print('\n' + persona_extrana + 'Hola, hola! ¿Sigues ahí? Ahora me están persiguiendo guardias alienígenas, no desaparezcas ahora!!')
        print('\n' + tu + 'Hola')
        print('\n' + persona_extrana + 'Hola, que bueno escuharte de nuevo! Dime, que hago ahora?!! El camino se bifurca. Tomo a la izquierda o la derecha!???\n')

        opcion = input('[OPCION (A) - Izquierda] | [OPCION (B) - Derecha]: ')

        if opcion == 'A': #Izquierda
            print('\n' + tu + '¡Izquierda!\n'
                  '\n' + persona_extrana + 'Bien, veo una escotilla semiabierta en la pared. Voy a entrar allí.\n'
                  '\n' + tu + '...\n'
                  '\n' + persona_extrana + '...\n'
                  '\n' + persona_extrana + 'Está oscuro aquí y mojado. No veo mucho.\n'
                  'Tengo algo de miedo, pero seguiré avanzando.'
                  '\nEsta prisión subterranea parece estar más al fondo todavía.\n'
                  'Por cierto, que bueno que no se ha perdido la conexión.\n'
                  '\n' + tu + 'Eh, recién comenzamos hablar.\n'
                  '\n' + persona_extrana + 'No, llevamos horas hablando. Me ayudaste a escapar de mi celda, ¿no recuerdas?\n'
                  '¡Oh! Por fin algo de luz. '
                  'Aquí hay unos interrumpores. Voy a encenderlos a ver.\n')

            opcion = input('[OPCION (A) - Aconsejarle no hacerlo] | [OPCION (B) - Incentivarlo hacerlo]: ')

            Interuptor = False

            if opcion == 'A':
                print('\n' + tu + '¡No toques nada!, no sabemos que pueda pasar.\n'
                      '\n' + persona_extrana + 'Vale, vale, no hay problema.\n')

            elif opcion == 'B':
                print('\n' + tu + 'Vale, quizás nos ayudan a salir de esto.\n'
                      '\n' + persona_extrana + 'Los moví todos. No parece que cambiara nada.\n'
                      '\n' + tu + 'No importa.\n')
                Interuptor = True

            print(tu + 'Oye, quiero aclarar que estas equivocado. Comezamos a hablar hace unos minutos,'
                  '\ncuando encendí mi Walkie Talkie. Creo que me confundes con alguien más. '
                  '¿Crees que me puedas ayudar a escapar de aquí?\n'
                  '\n' + persona_extrana + 'Veré que puedo hacer. Aquí hay unas llaves, ¿las debería coger?\n')

            opcion = input('[OPCION (A) - Coger las llaves] | [OPCION (B) - No coger las llaves]: ')

            llave_en_el_inventario = False

            if opcion == 'A':
                print('\n' + tu + 'Cogelas, ¿por qué no? Podrían ser utiles más adelante.\n'
                      '\n' + persona_extrana + 'Vale.\n')
                llave_en_el_inventario = True

            elif opcion == 'B':
                print('\n' + tu + 'No cojas las llaves. No creo que hagan falta, solo estorbarían y harían ruido.\n')

            nombre_cambiado = False
            preguntar_nombre = input('[OPCION (A) - Preguntar nombre] | [OPCION (B) - No preguntar]: ')

            if preguntar_nombre == 'A':
                print('\n' + tu + 'Por cierto, ¿cuál es tu nombre?\n'
                      '\n' + persona_extrana + 'La verdad es que no recuerdo. No sé, la persona anterior me llamaba Beta.'
                      '\n¿Cuál es el tuyo?\n')
                persona_extrana = 'Beta: '
                print(tu + 'Lo único que me viene a la mente es "Uno-punto-cero".')
                tu = '1.0: '
                nombre_cambiado = True
            elif preguntar_nombre == 'B':
                pass
            else:
                print('\nNo has elegido ninguna opción válida.')
                exit()
            print('\n' + persona_extrana + 'Necesito encontrar una salida de aquí.')
            print('\nHaz llegado hasta aquí. Parece que entiendes muy bien la bases del juego. Vamos a complejizarlo un poco.\n')

            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operacion = random.choice(["+", "-", "*"])
            operacion_aritmetica = str(num1) + operacion + str(num2)
            respuesta = eval(operacion_aritmetica)

            if nombre_cambiado:
                print(persona_extrana + 'Uno-punto-cero, no sé qué decirte tienes tienes la misma voz que la persona de antes.'
                                               '\nOh, espera, parece que aquí hay una puerta con un código.\n')
            else:
                print(persona_extrana + 'No sé qué decirte tienes tienes la misma voz que la persona de antes.'
                                               '\nOh, espera, parece que aquí hay una puerta con un código.\n')
            if Interuptor:
                print('Gracias a los interruptores encendidos anteriormente, persona_extrana puede ver una nota que sirve como pista.'
                      '\nEl código es ' + operacion_aritmetica)
            else:
                print('Está demasiado oscuro para ver claramente, pero puedo intentar adivinar.')

            opcion = int(input('\n¿Cuál es el código? '))

            if opcion == respuesta:
                print('\n' + persona_extrana + 'La puerta se abre...\n')
                print(tu + 'Bien hecho, ¿qué ves?\n')
                print(persona_extrana + 'Parece ser otro pasillo, pero este está mejor iluminado. Hay varias puertas a lo largo del pasillo.\n')
                print(tu + 'Debemos ser cuidadosos. ¿Hay alguna señal o algo que nos indique cuál puerta elegir?\n' +
                                  '\n' + persona_extrana + 'No.\n')

                puerta_correcta = random.choice(['A', 'B', 'C'])
                puertas_intentadas = []

                while len(puertas_intentadas) < 3:
                    opcion = input('[OPCION (A) - Primera puerta] | [OPCION (B) - Segunda puerta] | [OPCION (C) - Tercera puerta]: ').upper()

                    if opcion in puertas_intentadas:
                        print('\nYa intentaste con esa puerta. Elige otra.')
                        continue

                    if opcion == puerta_correcta:
                        if llave_en_el_inventario:
                            print('\nUsas la llave y la puerta se abre.\n')
                            print(tu + '¿Qué ves? ¿Encontraste alguna salida?\n')
                            print(persona_extrana + 'Parece que nunca hubo una salida. Solo veo un Walkie-Talkie y un espejo.\n')
                            print('Bien jugado. Fin del juego.')
                            exit()
                        else:
                            print('\n' + persona_extrana + 'La puerta no abre, ojalá tuviera alguna llave o algo. No!!!, se escuchan '
                                                   'guardias llegar.\n'
                                                   '\nFin del juego.\n')
                            exit()

                    if len(puertas_intentadas) == 3:
                        print('\n' + persona_extrana + 'La puerta no abre, ojalá tuviera alguna llave o algo. No!!!, se escuchan'
                                                      'guardias llegar.\n'
                                                      '\nFin del juego.\n')
                        exit()

                    print('\nLa puerta no es la correcta. Intenta con otra.\n')

            else:
                print('\n' + persona_extrana + 'La puerta no se abre. Esta sonando una alarma. Guardias!!! NO!!!!!\n')
                print('Fin del juego.')
                exit()
        elif opcion == 'B': #Derecha
            print('\n' + tu + '¡Derecha!\n'
                  '\n' + persona_extrana + 'Bien, veo una puerta semiabierta. Voy a entrar allí.\n'
                  '\n' + tu + '...\n'
                  '\n' + persona_extrana + '...\n'
                  '\n' + persona_extrana + 'Veo dos pasillos circulares, pero no veo el final de ninguno de los dos, '
                                           '¿tomo el de la derecha o el de la izquierda?\n')

            opcion = input('[OPCION (A) - Izquierda] | [OPCION (B) - Derecha]: ')

            if opcion == 'A':  # Izquierda_final_malo
                print('\n' + tu + 'Toma la izquierda.\n')
                print(persona_extrana + 'La habitación esta cada vez más oscura... Ah!!!!!!!!!\n'
                      '\n' + tu + 'Hola, Hola!!! ¡Responde!!!!\n')
                print('Nunca más hubo respuesta. Nunca escaparas.\n'
                      '\nFin del juego.')
                exit()
            elif opcion == 'B': # Derecha_final_bueno
                print('\n' + tu + 'Toma la derecha.\n')
                print(persona_extrana + 'Espera, veo una luz al final.\n')
                print(tu + '¿Es una salida?\n')
                print(persona_extrana + 'Sí, parece serlo.\n')
                print(tu + 'Entonces, ¿has escapado?\n')
                print('Un horrible sonido se comienza a escuhar por el Walkie-Talkie.\n'
                      'La comunicación se corta abruptamente. Te quedas solo, reflexionando sobre tu destino incierto.\n'
                      'Quizás persona_extrana escapo.\n'
                      'De momento, tu habitación se abre, sales con el Walkie-Talkie en mano. Escuchas pasos acercadose.\n'
                      'Comienzas a huir!\n'
                      '\n...\n'
                    '\nFin del juego.')
                exit()
    elif opcion == 'B': #final
        print('\nEstás seguro? Esta podría ser tu única oportunidad de comunicarte con alguien.\n')
        respuesta = input('[OPCION (A) - Sí] | [OPCION (B) - No]: ')

        if respuesta == 'A':
            print('\nDecides quedarte en la oscuridad. El silencio es tu única compañía. Mueres...\n'
                  'Fin.')
            exit()
        elif opcion == 'B': #comeinzo_del_juego_otra_vez
            if intentos >= 1:
                print('\nLo siento, ya tuviste suficientes intentos. Moriste!')
                exit()
            intentos += 1
            print('\nVamos a intentarlo de nuevo')
        else:
            print('\nNo has elegido ninguna opción válida.')
            exit()