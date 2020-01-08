from arrays import Arrays

simple = Arrays.create_simple_array(10, 4)
rand = Arrays.create_random_array(20, -7, 8)
Arrays.print_in_line(simple)
Arrays.print_in_line(rand)
print(len(Arrays.find_in_array(rand, -1, 1)))
