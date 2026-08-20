def rail_fence_encrypt(text, key):
    rail = ['' for _ in range(key)]

    row = 0
    direction = 1

    for ch in text:
        rail[row] += ch

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    cipher = ''.join(rail)
    return cipher


text = input("Enter Plain Text: ")
key = int(input("Enter Depth (Key): "))

cipher = rail_fence_encrypt(text, key)

print("Encrypted Text:", cipher)