# Exemple de matrice 2D (liste de listes)
matrix = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

def decrypt_matrix(matrix):
    secret_message = ""
    rows = len(matrix)
    cols = len(matrix[0])
    print(f"Rows: {rows}, Columns: {cols}")
    
    # Lire colonne par colonne
    for col in range(cols):
        for row in range(rows):
            char = matrix[row][col]
            if char.isalpha():
                secret_message += char
            else:
                # Remplacer les symboles entre lettres par un espace
                if secret_message and secret_message[-1] != ' ':
                    secret_message += ' '
    
    # Nettoyer les espaces multiples
    return ' '.join(secret_message.split())

print(decrypt_matrix(matrix))   