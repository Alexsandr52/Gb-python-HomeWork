class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __str__(self):
        matrix_str = str()
        for element in self.matrix:
            for el in element:
                matrix_str += f'{el:02} '
            matrix_str += '\n'
        return matrix_str

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return 'Matrix sizes aren\'t equal'
            
        new_matrix = self.matrix
        for i in range(len(self.matrix)):    
            if len(self.matrix[i]) != len(other.matrix[i]):
                return 'Matrix sizes aren\'t equal'
            for j in range(len(self.matrix[i])): 
                new_matrix[i][j] += other.matrix[i][j]
        return Matrix(new_matrix)

my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
my_matrix3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(my_matrix3)
print(my_matrix)
print(my_matrix + my_matrix2 + my_matrix3)
