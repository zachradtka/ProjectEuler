import sys

def num_paths():

    prev = [1,2]
    curr = [1]

    i = 1

    while True:
        
        yield prev[-1]
        # Increment i
        i+=1
        for j in range(1,i):
            curr.append(curr[j-1] + prev[j])

        # Double the last item to get the length
        curr.append(curr[-1]*2)


        # Re-initialize prev and curr
        prev = list(curr)
        curr = [1]


def main():
    grid_size = long(sys.argv[1])

    dim = 1
    for paths in num_paths():
        print('%d: %d' % (dim, paths))
        if grid_size == dim:
            break
        dim+=1

if __name__ == '__main__':
    main()