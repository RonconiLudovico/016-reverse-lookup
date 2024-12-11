#The following function demonstrates reverseLookup returning multiple, signle and no key
def main(dict):
    x = reverseLookup(dict, 'a')
    y = reverseLookup(dict, 'b')
    z = reverseLookup(dict, 'd')

    return x, y, z

#the following function finds all the key associated to a given value
def reverseLookup(dict, value):
    keys = [i for i in dict if dict[i] == value]

    return keys


if __name__ == '__main__':
    dictionary = {1 : 'a', 2 : 'b', 3 : 'b', 4 : 'b', 5 : 'c'}
    print(main(dictionary))
