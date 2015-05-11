def generate_fibonacci():
    indx = 1

    n_prev = 0
    n = 1
    
    yield (indx, n)

    while True:
        sum = n + n_prev
        n_prev = n
        n = sum
        
        indx+=1
        yield (indx, sum)
        
def main():
    for (i, j) in generate_fibonacci():
        if len(str(j)) == 1000:
            print('%d: %d' % (i,j)) 
            break

if __name__ == '__main__':
    main()