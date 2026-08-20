def generate_key_table(key):
    key = key.upper().replace("J", "I")
    table = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            used.add(ch)
            table.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J is omitted
        if ch not in used:
            table.append(ch)

    matrix = [table[i:i+5] for i in range(0, 25, 5)]
    return matrix


def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "Z"
            i += 1

    return result


def encrypt(matrix, text):
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:  # Same column
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:  # Rectangle rule
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


key = input("Enter Key: ")
plaintext = input("Enter Plain Text: ")

matrix = generate_key_table(key)

print("\nKey Matrix:")
for row in matrix:
    print(" ".join(row))

prepared = prepare_text(plaintext)
print("\nPrepared Text:", prepared)

cipher = encrypt(matrix, prepared)
print("Encrypted Text:", cipher)