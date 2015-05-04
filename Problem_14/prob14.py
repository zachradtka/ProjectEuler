import sys

def generate_collatz(start):
    if start > 1:
        if start%2 == 0:
            result = start/2
            yield result

        else:
            result = 3*start + 1
            yield result

        for val in generate_collatz(result):
                yield val

def main():
    end = long(sys.argv[1])

    max_chain = 0
    max_chain_start=1

    for i in range(1, end):


        seq = [i]
        
        for val in generate_collatz(i):
            seq.append(val)

        if len(seq) > max_chain:
            max_chain = len(seq)
            max_chain_start = seq[0]

    print('%d has length %d' % (max_chain_start, max_chain))

if __name__ == '__main__':
    main()