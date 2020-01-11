from random import randint
import copy


class matrix():

    @staticmethod
    def create(x, y):
        value = 0
        matrix = [[value for _ in range(y)] for _ in range(x)]
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

    @staticmethod
    def create_unix(x):
        unix = matrix.create(x, x)
        counter = 0
        for elem in unix:
            elem[counter] = 1
            counter += 1
        return unix

    @staticmethod
    def fill_random(matrix, m, n):

        for elem in matrix:
            for c in range(len(elem)):
                elem[c] = randint(m, n)
        return matrix

    @staticmethod
    def transpose(m):
        new_matrix = [[m[x][y] for x in range(len(m))]
                      for y in range(len(m[0]))]
        return new_matrix

    @staticmethod
    def create_diagonal(x, m, n):
        matrix = [[0 for _ in range(x)] for _ in range(x)]
        counter = 0
        for elem in matrix:
            elem[counter] = randint(m, n)
            counter += 1
        return matrix

    @staticmethod
    def compare_easy(matrix1, matrix2):
        # ???
        if matrix1 == matrix2:
            print('Macierze są równe.')
        else:
            print('Macierze nie są równe.')

    @staticmethod
    def compare(matrix1, matrix2):
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            counter = 0
            for elem in matrix1:
                for inner in elem:
                    if inner == matrix2[counter][elem.index(inner)]:
                        continue
                    else:
                        print('Macierze nie są równe.')
                        return False
                counter += 1
            print('Macierze są równe.')
            return True
        else:
            print('Macierze nie są równe.')
            return False


m = matrix.create(4, 3)
u = matrix.create_unix(5)
r = matrix.create(3, 5)
r = matrix.fill_random(r, 5, 9)
t = matrix.create(3, 5)
t = matrix.fill_random(t, 1, 9)


print('\n6: ')
matrix.print(u)

print('\n7: ')
matrix.print(r)

print('\n8: ')
matrix.print(t)
t = matrix.transpose(t)
print('Transponowana: ')
matrix.print(t)

print('\n21: ')
# diagonalna 3x5??
d = matrix.create_diagonal(5, 10, 50)
matrix.print(d)

print('\n22: ')
t1 = matrix.create(3, 5)
t1 = matrix.fill_random(t1, 7, 13)
t2 = matrix.create(3, 5)
t2 = matrix.fill_random(t2, 8, 12)

matrix.print(t1)
print('')
matrix.print(t2)
matrix.compare_easy(t1, t1)
matrix.compare(t1, t1)
