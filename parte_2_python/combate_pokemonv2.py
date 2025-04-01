from random import randint
import os
import readchar

PIKACHU = """           .     .           .               .                      .  .     
   .                                   .          .   .         .....        
                          .                          .      ....:@@# .  .    
            .                             .            .    ..-%%@@#         
    .                            .                    ...   #%***@@#         
.             .               .             .        .....-@#**@@@@#         
                            .            .         . .....-@#**@@@@# .       
      .:-------. ..........            .            ....:=+.=*@@@@%+.  .     
      .#@######****-.......                         ...:+:..:-@@@@=..    .   
.  .. ...%@%***********+..... ... .      .    ..    ..==...::::@@@=         .
         @@@@@@@#**=....-=++=.......        .   ......--...::::*#@=.         
         .-##%@@@@@*........:==-.:..            .....=:..::::::@%.. .   .    
          .  -+@@@@*::::::::::::-=--.........    ..--:..:::::-=+=..  .       
             ..:--#+:::::::::::::::-+++:..... .....==..:::::-=%....  .    .  
             ... ..-#@*::::::::::::::::=*#@@@@@@:-#:..::::::-=@....          
 . .          .  .....=@@+::::::::=++=........::=++:.::::::-*+...            
...              ........=##*=--==-:............:::::::::--=**  .            
.........   .             ..-%=-::::.........:::::::::::--=%:..              
---.......    .          ..*+-.::.::......:::::::::::::::--=++.        ..    
...-=++:...................--.::.::.::.:::::::::::::::::::::%#..   .  .      
.......=====.............-=.::.::.::..:::::::::::::::::::::::-@....  .       
::....::::::====-::::...:--::::::::.::::::::::::::::::::::::*#@--..          
+-..:::::::::::::::::++++-::::::::::::::::::::::::::::::::::::-@%..         .
+=..:::::::::::::::::::::+#@#::::::::::::::::::::::::::::::::::--#- .    .   
.:-.::::::::::::::::::::::::-#@*::::::::::::::::::::::::::::::-+*@= ..      .
.:+.:::::::::::::::::::::::::::+@::::::::::::::::::::::::::::-++*@=.  .      
.:+.:::::::::::::::::::::::::::+@:::::::::::::::::::::::::::-=#***-       .  
...-:.::::::::::::::::::::::::*+-:::::::::::::::::::::::::::*##@%..     .    
...+-.::::::::::::::::::::::::@*::::::::::::::::::::::::::-+##@....          
...+-:::::::::::::::::::::::::%*::::::::::::::::::::::::::::++.............. 
...+**************+===-:::::=#--=--=======---::::::::::::::::-+++----++:::.. 
....... .        ..-*--::::++***+**#****##***+++=-:::::::::::::::----------. 
                 .*=.::---:@%*++####***#******###*+=-:::::::::::::::::::**.. 
        .   . ....*=.----+*=++**+*############*++=::::::::::::::::::::::::#: 
             ...=*:::----+***%%%%@+:::::::::::::::::::::::::::::::::::::++.. 
     .      ...-==::-----------=**-:::::::::::::::::::::::--++-------==+==.. 
   .        ...*####%%%%*=-===#*=:::::::::::::::::::::::----%@%%%%%%%-:-.    
 .          .......-*:+@++++*@##########*+++:::::::::-------%#........... .  
            .......-+@%#*##@%*#*#############+=::-----------%#.........      
        ..       .:+%*####%#################**+=------------##..   .. . .    
                 .*#%%###*##%%=================-------------=+*..            
                 .*+==+@@#####%*-----------------------------=@       
                            """
SQUIRTLE = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⠛⠉⠉⠀⠀⠀⠀⠀⠀⠉⠙⠻⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⢻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠿⣷⣄⠀⠀⠈⠛⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣇⣀⣿⣿⡆⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠟⠋⠁⢀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⢿⣿⣿⡿⠁⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣦⡀⠀⢈⣡⣴⣶⣶⣤⣤⣤⣀⣀⣀⡀⠀⢀⣉⢁⣤⣴⠆⠀⠀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⠿⠟⠋⠁⠀⠀⠈⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠀⢠⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⡋⣿⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⡶⠿⢻⣿⣿⠷⣶⣤⣤⣄⣀⣀⣀⣀⣀⣀⣠⣤⣾⣿⠿⢿⣾⣿⣶⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣶⠿⠛⠋⠀⠠⣤⣾⠋⠁⢶⣤⣈⠉⠙⠛⠛⠛⠛⢛⣿⡿⠋⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⣀⣤⣶⠟⠋⠀⠀⠀⠀⠀⣾⣿⣧⣀⠀⠀⠉⠿⢷⣦⣀⠀⠀⢀⣾⠟⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⠉⠻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⣿⣿⣯⣾⠂⠀⠀⠀⠀⠀⣸⡿⠀⠉⠛⠷⠶⣦⣤⣤⣈⣉⣀⣠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⡄⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣿⣿⣿⣧⣤⡀⠀⠀⠀⣴⣿⠀⠀⠀⠀⠀⠀⠀⠈⣿⠉⠉⠉⣽⡟⠀⣀⣀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠀⠀⢹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣿⣿⣌⣝⣿⣶⣶⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⢠⣿⣠⣾⣯⣿⡄⠀⣀⠀⠀⢀⣼⡟⢸⡿⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⢻⣇⠀⠀⠀⠀⠀⠀⢸⡿⠀⢠⣾⠋⠁⠈⢿⣿⣷⡿⢛⣿⣷⣿⠋⠀⣼⡇⢶⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠈⣿⣆⠀⠀⠀⠀⠀⣼⠇⠀⠛⠛⠿⣷⣦⣤⣀⣙⣿⣿⠿⣻⡟⠀⢀⣿⣀⣾⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⣿⠛⠛⠛⠿⢶⣶⣿⣦⣤⣤⣤⣤⣤⣀⣽⡿⠋⠉⠀⠀⣿⣧⠀⢸⣿⣿⣇⣿⣿⣿⠀⠀⠀⢀⣠⣴⡾⠿⠿⠻⠿⣶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠀⠀⠀⠀⠀⠀⣿⡅⠈⠉⠉⠉⠉⠉⠙⢿⣄⠀⠀⣤⣙⣿⣄⠀⣿⣿⣿⣿⣿⠇⠀⢀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠹⢿⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⢿⣧⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀⠀⣀⣤⠈⣻⣿⠿⠛⠛⠛⠻⣷⣿⣿⢿⣿⡿⠀⣰⡿⠁⠀⠀⠀⠀⠀⢀⣴⠞⠃⠀⠰⣿⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⢻⣧⡀⠀⠀⠀⠀⣿⡄⠀⠀⣀⣤⡾⠛⢁⣿⠟⠁⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣡⣾⠟⠀⠀⠀⠀⢀⣴⡶⠿⢿⣦⡄⠀⠀⢻⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠙⣷⣔⣲⣶⣶⣿⣷⣶⡞⠋⠁⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡟⠁⠀⠀⠀⠀⣴⣿⠋⠀⠀⠀⠈⠁⠀⠀⢸⣿⠇
⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠈⢿⣿⣏⡉⡀⠈⠙⣿⢷⣶⣤⣾⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠋⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠈⣻⣿⢶⣶⣤⣟⣀⣀⣉⣹⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡆⠀⠀⠀⠀⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀⢠⣾⡿⠃⠀
⠀⠀⠀⠀⠀⠀⣠⣼⣿⠇⠀⠀⠀⠀⠀⠀⢀⣿⡿⠁⠀⠀⠉⠉⠉⠉⠛⠿⠿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⣀⡀⠀⠀⠀⠀⠀⠈⠛⠿⣶⣤⣤⣴⡾⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠸⣿⣿⣿⣠⣤⠀⠀⢠⣤⣤⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠛⠛⠻⠿⠶⢶⣶⣶⣶⠾⠿⠟⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠛⠛⢻⣿⣷⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣶⣦⣤⡀⠀⣤⣤⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠉⠛⠿⠟⠁⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            """
OBSTACLE_DEFINITION = """\
                                             
                                             
                                             
                                             
                                             
   #########                                 
                                             
               ################              
               ############                  
               #####                         
                    ######                   
                ################             
                                             
                                             
                                             
     ########           ##################   
                                             
                                             
            ###########                     \
"""
POS_X = 0
POS_Y = 1
USER = " @"
POKEMON_TRAINER = " *"
MAP_WIDTH = 45
MAP_HEIGHT = 18
TRAINERS = 2
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 95
TAMANO_BARRA_VIDA = 20
ATACKS = ["B", "C", "O", "N", "S"]

obstacle_definition_map = [list(row) for row in OBSTACLE_DEFINITION.split("\n")]

def battle():
    vida_pikachu = VIDA_INICIAL_PIKACHU
    vida_squirtle = VIDA_INICIAL_SQUIRTLE
    # Se desenvuelven los turnos del combate
    while vida_pikachu > 0 and vida_squirtle > 0:
        os.system("clear")
        # Turno de Pikachu
        # Pikachu back ASCII art
        print(PIKACHU)
        print("Turno de Pikachu")
        ataque_pikachu = None
        while ataque_pikachu not in ATACKS:
            ataque_pikachu = input("¿Qué ataque deseas realizar? [B]ola voltio, [C]arga, "
                                   "[O]nda Trueno, [N]ada, [S]alir del combate: ").capitalize()
        if ataque_pikachu == "B":
            # Bola voltio
            print("Pikachu ataca con Bola Voltio")
            vida_squirtle -= 10
        elif ataque_pikachu == "C":
            print("Pikachu ataca con Carga")
            vida_squirtle -= 13
        elif ataque_pikachu == "O":
            print("Pikachu ataca con Onda Trueno")
            vida_squirtle -= 11
        elif ataque_pikachu == "N":
            print("Pikachu no hace nada...")
        elif ataque_pikachu == "S":
            break

        if vida_squirtle <= 0:
            vida_squirtle = 0
            break
        barra_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
        print("Pikachu: [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu,
                                               " " * (TAMANO_BARRA_VIDA - barra_de_vida_pikachu),
                                               vida_pikachu, VIDA_INICIAL_PIKACHU))

        barra_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
        print("Squirtle: [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle,
                                                " " * (TAMANO_BARRA_VIDA - barra_de_vida_squirtle),
                                                vida_squirtle, VIDA_INICIAL_SQUIRTLE))
        input("Enter para continuar...\n\n")
        os.system("clear")

        # Turno Squirtle
        # Squirtle ASCII art
        print(SQUIRTLE)
        print("Turno Squirtle")

        ataque_squirtle = randint(1, 3)
        if ataque_squirtle == 1:
            print("Squirtle ataca con Placaje")
            vida_pikachu -= 10
        elif ataque_squirtle == 2:
            print("Squirtle ataca con Pistola Agua")
            vida_pikachu -= 12
        elif ataque_squirtle == 3:
            print("Squirtle ataca con Burbuja")
            vida_pikachu -= 9
        if vida_pikachu < 0:
            vida_pikachu = 0
        barra_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
        print("Pikachu: [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu,
                                               " " * (TAMANO_BARRA_VIDA - barra_de_vida_pikachu),
                                               vida_pikachu, VIDA_INICIAL_PIKACHU))

        barra_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
        print("Squirtle: [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle,
                                                " " * (TAMANO_BARRA_VIDA - barra_de_vida_squirtle),
                                                vida_squirtle, VIDA_INICIAL_SQUIRTLE))
        input("Enter para continuar...\n\n")
        os.system("clear")
    if vida_pikachu > vida_squirtle:
        print("Pikachu gana!")
        input("Enter para continuar...\n\n")
        return False
    else:
        print("Squirtle gana!")
        input("Enter para continuar...\n\n")
        return True



def main():
    my_position = [2, 0]
    trainer_positions = [[37, 3], [41, 16]]
    while True:
        # Draw game
        # clear old map
        restart_map = False
        os.system("clear")
        print("#" * MAP_WIDTH * 2 + "#" * 2)
        position = None
        for coordinate_y in range(MAP_HEIGHT):
            print("#", end="")
            for coordinate_x in range(MAP_WIDTH):
                to_draw = "  "
                for position in trainer_positions:
                    if coordinate_y == position[POS_Y] and coordinate_x == position[POS_X]:
                        to_draw = POKEMON_TRAINER
                        break
                if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                    # combat
                    if to_draw == POKEMON_TRAINER:
                        lose_combat = battle()
                        if lose_combat:
                            os.system("clear")
                            exit("Game Over")
                        else:
                            trainer_positions.remove(position)
                            restart_map = True
                            if not trainer_positions:
                                exit(f"Derrotaste a los {TRAINERS} entrenadores. You WIN!!!!!!!!!!!!!!")
                    to_draw = USER
                if obstacle_definition_map[coordinate_y][coordinate_x] == "#":
                    to_draw = "##"
                print(f"{to_draw}", end="")
                if restart_map:
                    break
            if restart_map:
                break
            print("#")
        if restart_map:
            continue
        print("#" * MAP_WIDTH * 2 + "#" * 2)
        # Move user
        new_position = None
        direction = readchar.readchar()
        if direction == "w":
            new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
        elif direction == "s":
            new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
        elif direction == "a":
            new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
        elif direction == "d":
            new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
        elif direction == "q":
            exit("Adiós")
        if new_position:
            if obstacle_definition_map[new_position[POS_Y]][new_position[POS_X]] != "#":
                my_position = new_position
if __name__ == "__main__":
    main()