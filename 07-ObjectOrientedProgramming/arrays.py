import random


class arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def print_in_line(array):
        print(*array, sep=',')

    @staticmethod
    def create_simple_array(number, elem):
        arr = []
        for _ in range(number):
            arr.append(elem)
        return arr

    @staticmethod
    def create_random_array(number, low, high):
        arr = []
        for _ in range(number):
            arr.append(random.randint(low, high))
        return arr

    @staticmethod
    def find_in_array(array, low, high):
        arr = []
        for elem in array:
            if elem in range(low, high+1):
                arr.append(elem)
        return arr


""" 
my_array = [4, 1, 8, 7, 2]
arrays.print_in_col(my_array)
arrays.print_in_line(my_array)
arrays.print_in_line(arrays.create_simple_array(12, 3))
arrays.print_in_line(arrays.create_random_array(12, 11, 65))
arrays.print_in_line(arrays.find_in_array(my_array, 1, 4))
 """
