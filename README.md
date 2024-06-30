import tkinter as tk
from tkinter import messagebox

# Reglas del juego

rules = {
    "tijeras": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["tijeras", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["tijeras", "piedra"]
}

choices = list(rules.keys())

# Función para jugar una ronda

def play_game(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "Empate"
    elif player2_choice in rules[player1_choice]:
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

# Función para manejar la lógica del juego

def handle_game():
    global player1_score, player2_score
    
    player1_choice = player1_var.get().lower()
    player2_choice = player2_var.get().lower()
    
    if player1_choice not in choices or player2_choice not in choices:
        messagebox.showerror("Error", "Elección inválida. Por favor, elija nuevamente.")
        return
    
    result = play_game(player1_choice, player2_choice)
    
    if result == "Jugador 1 gana":
        player1_score += 1
    elif result == "Jugador 2 gana":
        player2_score += 1
    
    result_label.config(text=f"Jugador 1: {player1_choice}, Jugador 2: {player2_choice} -> {result}")
    score_label.config(text=f"Marcador -> Jugador 1: {player1_score}, Jugador 2: {player2_score}")

# Función para reiniciar el juego

def reset_game():
    global player1_score, player2_score
    player1_score = 0
    player2_score = 0
    result_label.config(text="")
    score_label.config(text="Marcador -> Jugador 1: 0, Jugador 2: 0")

# Variables de puntaje

player1_score = 0
player2_score = 0

# Crear ventana principal

root = tk.Tk()
root.title("Piedra, Papel, Tijeras, Lagarto, Spock")

# Etiquetas y campos de entrada para las elecciones de los jugadores

player1_label = tk.Label(root, text="Jugador 1, elige entre tijeras, papel, piedra, lagarto, spock:")
player1_label.pack()
player1_var = tk.StringVar()
player1_entry = tk.Entry(root, textvariable=player1_var)
player1_entry.pack()

player2_label = tk.Label(root, text="Jugador 2, elige entre tijeras, papel, piedra, lagarto, spock:")
player2_label.pack()
player2_var = tk.StringVar()
player2_entry = tk.Entry(root, textvariable=player2_var)
player2_entry.pack()

# Botón para jugar una ronda

play_button = tk.Button(root, text="Jugar", command=handle_game)
play_button.pack()

# Botón para reiniciar el juego

reset_button = tk.Button(root, text="Reiniciar", command=reset_game)
reset_button.pack()

# Etiqueta para mostrar el resultado

result_label = tk.Label(root, text="")
result_label.pack()

# Etiqueta para mostrar el marcador

score_label = tk.Label(root, text="Marcador -> Jugador 1: 0, Jugador 2: 0")
score_label.pack()

# Iniciar el bucle de la interfaz gráfica

root.mainloop()
