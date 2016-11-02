'''
    This program is used to find the LCS (Longest common words). 
    This is a Bottom up Dynamic Programming approach
    Complexity = O (nxm)
    for n = len(S), m = len(T)

    @author: veng.thai@gmail.com
'''

print(__doc__)

import sys

'''
################################################################################################
    use to display the matrix in a friendly way
################################################################################################
'''
def print_matrix(matrix):
    print('')
    for row in matrix:
        for column in row:
            print(column, end=' ')
        print('')
    print('')

'''
################################################################################################
    print the result sequence
################################################################################################
'''
def print_sequence(matrix, T):
    i = len(matrix) - 1
    j = len(matrix[0]) - 1

    lcs = matrix[i][j]

    count = 0
    result = []
    prev = (-1, -1)

    while count != lcs:
        if prev[0] == i and prev[1] == j:
            break
        else:
            prev = (i, j)

        top = i - 1 if i > 0 else 0
        left = j - 1 if j > 0 else 0

        #print('[%d,%d] = %d (top=%d, left=%d)' %(i, j, matrix[i][j], matrix[i-1][j], matrix[i][j-1]))
        if (matrix[i][j] > matrix[i-1][j] or i-1 < 0) and (matrix[i][j] > matrix[i][j-1] or j-1 < 0):
            #print(T[j])
            result.append(T[j])
            count += 1
            i = top
            j = left
        else:
            if matrix[i-1][j] == matrix[i][j]:
                i = top
            elif matrix[i][j-1] == matrix[i][j]:
                j = left

    print('LCS = %d\n' %lcs)
    [print(x, end='') for x in result[::-1]]
    print('\n')

'''
################################################################################################
    main method
################################################################################################
'''
def main():
    S = sys.argv[1]
    T = sys.argv[2]

    print('\nS = %s, T = %s' %(S, T))

    w = len(T)
    h = len(S)
    matrix = [x[:] for x in [[0] * w] * h]

    for column in range(0, len(T)):
        for row in range(0, len(S)):
            #print('Before:', S[row], T[column], matrix[row-1][column], matrix[row][column-1])
            top = row - 1 if row > 0 else 0
            left = column - 1 if column > 0 else 0
            if T[column] != S[row]:
                matrix[row][column] = max(matrix[top][column], matrix[row][left])
            else:
                matrix[row][column] = matrix[top][left] + 1
                #print_matrix(matrix)

    print_matrix(matrix)
    print_sequence(matrix, T)


if __name__ == "__main__":
    main()