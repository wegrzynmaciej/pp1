import random


class Arrays():
    separator = ','

    @staticmethod
    def change_separator_noinput(new_separator):
        Arrays.separator = new_separator

    @staticmethod
    def change_separator_input():
        Arrays.separator = input("Podaj nowy separator: ")

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def print_in_line(array):
        print(*array, sep=Arrays.separator + ' ')

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


if __name__ == "__main__":
    my_array = [4, 1, 8, 7, 2]
    Arrays.print_in_col(my_array)
    Arrays.print_in_line(my_array)
    Arrays.print_in_line(Arrays.create_simple_array(12, 3))
    Arrays.print_in_line(Arrays.create_random_array(12, 1, 2))
    Arrays.print_in_line(Arrays.find_in_array(my_array, 1, 7))
    Arrays.change_separator_noinput('.')
    Arrays.print_in_line(my_array)
    Arrays.change_separator_input()
    Arrays.print_in_line(my_array)
