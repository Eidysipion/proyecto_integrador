
# PARTE  1:
nombre = input("ingrese el nombre de el jugador")
print("¡Bienvenid@! al juego ," , nombre)

 # PARTE  2:
import  readchar 

def main():
    while True:
        # Leer el carácter presionado
        key = readchar.readchar()
        
        # Imprimir el carácter presionado
        print(key)
        
        # Verificar si el carácter presionado es la flecha hacia arriba
        if key =='W':  # Código de escape para la flecha hacia arriba, con teclas WASD por configuracion del teclado
            break

if __name__ == '__main__':
    main()

 # PARTE  3:
import os
import msvcrt

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    number = 0

    while number <= 50:
        clear_terminal()
        print(number)
        
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if key == b'n':
                number += 1