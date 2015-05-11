CHAR_VALUE = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,
              'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
              'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
              'p':16, 'q':17, 'r':18, 's':19, 't':20,
              'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def main():

    # Read in the names from the file
    with open('input.txt', 'r') as ifp:
        names = ifp.readline()

    # Remove Quotes and turn the names into a list
    names = names.translate(None, '"')
    list_names = names.split(',')

    # Sort the names
    list_names.sort()

    value = 0
    position = 1

    for name in list_names:
        curr_value=0

        for letter in list(name.lower()):
            curr_value+=CHAR_VALUE[letter]

        value+=curr_value*position
        position+=1

    print('Total Score: %d' % (value))

if __name__ == '__main__':
    main()