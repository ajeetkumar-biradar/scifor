# Himanshi is confused
# with different shapes.Write a program in python to print different shapes using these symbols: “ | ”, “-”, “ / ”, “\”
print("Rectangle:")
for i in range(3):
    print("|" * 3)

print("\nTriangle:")
for i in range(1, 6):
    print("/" * i)

print("\nPyramid:")
for i in range(1, 5):
    spaces = " " * (4 - i)
    print(spaces + "\\" * (2 * i - 1))
