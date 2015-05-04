import sys

def read_grid(file_name):
    grid = list()

    with open(file_name, 'r') as ifp:
        for row in ifp:
            row = row.strip()
            grid.append([int(x) for x in row.split()])

    return grid


def display_grid(grid):
    for row in grid:
        print('%s' % (' '.join(str(x) for x in row)))

def seq_product(seq):
    prod = 1

    for i in seq:
        prod*=i

    return prod

def max_product(curr_max, new_prod):
    if new_prod > curr_max:
        return new_prod

    return curr_max

def largest_product(grid, seq_len):
    """
    Find the largest product in a grid with adjacent numbers len
    """

    max_prod = 0

    grid_dim = len(grid)

    # Cycle through grid
    for row in range(grid_dim):
        for col in range(grid_dim):

            # Check the product of the sequence to the left
            if col <= grid_dim - seq_len:
                seq = grid[row][col:(col+seq_len)]

                prod = seq_product(seq)
                max_prod = max_product(max_prod, prod)

            # Check the product of the sequence down
            if row <= grid_dim - seq_len:
                
                # Build a sequence
                seq = list()
                for i in range(seq_len):
                    seq.append(grid[row+i][col])

                prod = seq_product(seq)
                max_prod = max_product(max_prod, prod)

            # Check the product of the left diagonal sequence
            if (row <= grid_dim - seq_len) and (col <= grid_dim - seq_len):
                # Build a sequence
                seq = list()
                for i in range(seq_len):
                    seq.append(grid[row+i][col+i])

                prod = seq_product(seq)
                max_prod = max_product(max_prod, prod)


            # Check the product of the right diagonal sequence
            if (row <= grid_dim - seq_len) and (col >= seq_len-1) and (col <= grid_dim - seq_len):
                # Build a sequence
                seq = list()
                for i in range(seq_len):
                    seq.append(grid[row+i][col-i])

                prod = seq_product(seq)
                max_prod = max_product(max_prod, prod)


    return max_prod


def main():
    input_file = sys.argv[1]

    grid = read_grid(input_file)

    print('Max prod = %d' % (largest_product(grid, 4)))


    #display_grid(grid)


if __name__ == '__main__':
    main()

