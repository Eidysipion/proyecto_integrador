nombre = input("ingrese el nombre de el jugador")
print("¡Bienvenid@! al juego ," , nombre)

import  readchar 

def main():
    while True:
        # Leer el carácter presionado
        key = readchar.readchar()
        
        # Imprimir el carácter presionado
        print(key)
        
        # Verificar si el carácter presionado es la flecha hacia arriba
        if key =='W':  # Código de escape para la flecha hacia arriba
            break

if __name__ == '__main__':
    main()

