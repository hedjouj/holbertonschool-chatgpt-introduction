#!/usr/bin/python3

def print_board(board):
    """
    Affiche la grille du jeu dans un format lisible.

    Paramètres:
    board (list of list): La grille de jeu 3x3 contenant "X", "O", ou " ".

    Retour:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie s'il y a un gagnant sur la grille.

    Paramètres:
    board (list of list): La grille du jeu.

    Retour:
    str ou None: Le symbole du gagnant ("X" ou "O") si gagné, sinon None.
    """
    # Vérifie les lignes
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]

    # Vérifie les colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Diagonale principale
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    # Diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_full(board):
    """
    Vérifie si la grille est complètement remplie (match nul).

    Paramètres:
    board (list of list): La grille du jeu.

    Retour:
    bool: True si pleine, False sinon.
    """
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """
    Fonction principale du jeu : boucle de jeu, saisies des joueurs,
    vérification du gagnant ou de match nul.

    Paramètres:
    Aucun

    Retour:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Entrée sécurisée
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Please enter numeric values only.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

# Lancer le jeu
if __name__ == "__main__":
    tic_tac_toe()

