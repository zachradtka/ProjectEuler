import sys

def num_paths(grid_size, x, y, paths):
    # Move Right
    if x < grid_size:    
        paths=num_paths(grid_size, x+1,y, paths)
    
    # Move Down
    if x != 0 and y < grid_size:
        # If we reached 0 we are done counting half of the square
        paths=num_paths(grid_size, x, y+1, paths)


    # Have we reached the end
    if x == grid_size and y == grid_size:
        # Increase Pahts by 2 because we are counting the first half
        paths+=2

    return paths


def main():
    grid_size = long(sys.argv[1])

    paths = num_paths(grid_size, 0,0,0)
    print('%d paths found' % (paths))

if __name__ == '__main__':
    main()