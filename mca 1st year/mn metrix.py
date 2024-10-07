def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

# Input dimensions
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# Create and display the matrix
matrix = create_matrix(m, n)
print("The created matrix is:")
display_matrix(matrix)
