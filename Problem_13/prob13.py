import sys

def main():
    file_name = sys.argv[1]

    with open(file_name, 'r') as ifp:
        sum = 0
        for line in ifp:
            num = long(line.strip())
            sum += num

        print(sum)

if __name__ == '__main__':
    main()