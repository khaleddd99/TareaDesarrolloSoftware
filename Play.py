import random

rules = {
    "tijeras": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["tijeras", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["tijeras", "piedra"]
}

choices = list(rules.keys())

def play_game(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "Empate"
    elif player2_choice in rules[player1_choice]:
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

def play_rounds(num_rounds):
    player1_score = 0
    player2_score = 0
    
    for _ in range(num_rounds):
        player1_choice = random.choice(choices)
        player2_choice = random.choice(choices)
        result = play_game(player1_choice, player2_choice)
        
        if result == "Jugador 1 gana":
            player1_score += 1
        elif result == "Jugador 2 gana":
            player2_score += 1
        
        print(f"Jugador 1: {player1_choice}, Jugador 2: {player2_choice} -> {result}")
    
    if player1_score > player2_score:
        print("Jugador 1 es el ganador del juego")
    elif player2_score > player1_score:
        print("Jugador 2 es el ganador del juego")
    else:
        print("El juego terminó en empate")

def player_vs_player():
    player1_score = 0
    player2_score = 0
    
    while True:
        player1_choice = input("Jugador 1, elige entre tijeras, papel, piedra, lagarto, spock: ").lower()
        player2_choice = input("Jugador 2, elige entre tijeras, papel, piedra, lagarto, spock: ").lower()
        
        if player1_choice not in choices or player2_choice not in choices:
            print("Elección inválida. Por favor, elija nuevamente.")
            continue
        
        result = play_game(player1_choice, player2_choice)
        
        if result == "Jugador 1 gana":
            player1_score += 1
        elif result == "Jugador 2 gana":
            player2_score += 1
        
        print(f"Jugador 1: {player1_choice}, Jugador 2: {player2_choice} -> {result}")
        print(f"Marcador -> Jugador 1: {player1_score}, Jugador 2: {player2_score}")
        
        play_again = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if play_again != 's':
            break

import tkinter as tk
from tkinter import messagebox

def play_game_gui(player1_choice, player2_choice):
    result = play_game(player1_choice, player2_choice)
    messagebox.showinfo("Resultado", f"Jugador 1: {player1_choice}, Jugador 2: {player2_choice} -> {result}")

root = tk.Tk()
root.title("Piedra, Papel, Tijeras, Lagarto, Spock")

for choice in choices:
    btn = tk.Button(root, text=choice.capitalize(), command=lambda ch=choice: play_game_gui(ch, random.choice(choices)))
    btn.pack()

root.mainloop()
       

       

