#matrix questions
#1.logic based on questions
#ex: auxillary array ,using dynamic prog ,flag variables , two pointers
#bfs - bradth first search
#dfs - depth first search

"""
#q: given a 2d integer array n*n matrix , return the transpose matrix . the transpose of a matrix
is the matrix flipped over its main diagonal , switching the matrix row and column indices
"""

#transpose means interchanging of elements.


#logic : swap a[i][j] with a[j][i]  over the diagonal of matrix

#the space complexity concept:
#space complexity is O(1) BECAUSE WE are not using auxillary array
#SPACE COMPLEXITY IF WE USE AUXILLARY ARRAY -O(m,n)



#program:
def transpose_matrix(matrix):
    n = len(matrix)

    transpose = [[0] * n for _ in range(n)] #'_' repeats something

    for i in range(n):
        for j in range(n):
            transpose[j][i] = matrix[i][j]

    return transpose


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose_matrix(matrix))