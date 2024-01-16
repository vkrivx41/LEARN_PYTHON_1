
def get_string_methods():
    counter: int = 0

    for method in dir(str):
        if '__' not in method:
            counter += 1
            print(counter, method, sep=": ")


get_string_methods()
