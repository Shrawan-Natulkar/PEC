import math

text = input("Enter Plain Text: ").replace(" ", "").upper()

cols = int(input("Enter Number of Columns: "))

rows = math.ceil(len(text) / cols)

while len(text) < rows * cols:
    text += 'X'

matrix = []

k = 0
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(text[k])
        k += 1
    matrix.append(row)

print("\nMessage Rectangle:")
for row in matrix:
    print(" ".join(row))

print("\nEnter Column Order (Example: 3 1 4 2)")
order = list(map(int, input().split()))

cipher = ""

for col in order:
    for row in matrix:
        cipher += row[col - 1]

print("\nEncrypted Text:", cipher)