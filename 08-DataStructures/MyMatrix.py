from random import randint
import copy


class matrix():

    @staticmethod
    def create(x, y):
        value = 0
        matrix = [[value for i in range(y)] for j in range(x)]
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
        new_matrix = copy.deepcopy(matrix)

        for elem in new_matrix:
            for c in range(len(elem)):
                elem[c] = randint(m, n)
        return new_matrix


m = matrix.create(4, 3)
u = matrix.create_unix(5)
nm = matrix.create(3, 5)
r = matrix.fill_random(nm, 5, 9)
print('\n6: ')
matrix.print(u)
print('\n7: ')
matrix.print(r)
