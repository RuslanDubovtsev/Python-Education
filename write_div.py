def import_files(name, some_element):
    with open(name, 'a') as file:
        file.write(some_element)
        file.write('\n')