import pickle

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, -1)

def read_object(filename):
    with open(filename, 'rb') as input:
        return pickle.load(input)
        