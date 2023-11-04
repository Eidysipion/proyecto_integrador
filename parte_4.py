from typing import List, Tuple
import os

# Función para convertir el mapa de cadena en una matriz de caracteres
def string_to_maze(input_string: str) -> List[List[str]]:
    lines = input_string.strip().split('\n')
    maze = [list(line) for line in lines]
    return maze

# Función para limpiar la pantalla y mostrar el laberinto
def clear_and_display(maze: List[List[str]]):
    os.system('clear' if os.name == 'posix' else 'cls')  # Limpiar la pantalla
    for row in maze:
        print(''.join(row))

# Función principal del juego
def main_loop(maze: List[List[str], start: Tuple[int, int], end: Tuple[int, int]):
    px, py = start  # Posición inicial del jugador
    maze[px][py] = 'P'  # Colocar al jugador en la posición inicial

    while (px, py) != end:
        clear_and_display(maze)

        # Leer la entrada del teclado
        key = input("Use las teclas de flecha para mover al jugador. Presione 'q' para salir: ").lower()

        # Actualizar la posición del jugador según la tecla presionada
        if key == 'q':
            break
        elif key == 'w' and px > 0 and maze[px - 1][py] != '#':
            maze[px][py] = '.'
            px -= 1
        elif key == 's' and px < len(maze) - 1 and maze[px + 1][py] != '#':
            maze[px][py] = '.'
            px += 1
        elif key == 'a' and py > 0 and maze[px][py - 1] != '#':
            maze[px][py] = '.'
            py -= 1
        elif key == 'd' and py < len(maze[0]) - 1 and maze[px][py + 1] != '#':
            maze[px][py] = '.'
            py += 1

        maze[px][py] = 'P'  # Colocar al jugador en la nueva posición

    clear_and_display(maze)
    if (px, py) == end:
        print("¡Has llegado al final!")

# Ejemplo de uso
if __name__ == "__main__":
    maze_str = """#############
#P.#.......#
#.#.#######.#
#.#.#.....#.#
#.###.###.#.#
#...#.###.#.#
#.###.###.#.#
#.#.....#.#.#
#.#######.#.#
#.........#.#
#############"""

    maze = string_to_maze(maze_str)
    start_position = (0, 1)
    end_position = (len(maze) - 1, len(maze[0]) - 1)

    main_loop(maze, start_position, end_position)
