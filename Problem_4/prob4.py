def is_palindrome(num):
    mid = len(num)/2
    for i in range(mid):
        if num[i] != num[-(i+1)]:
            return False

    return True

def largest_possible_palindrome(num):
    largest = 0

    for i in reversed(range(num)):
        for j in reversed(range(num)):
            result = i*j
            if is_palindrome(str(result)) \
               and (result > largest):
                
                largest = result
    return largest

def main():
    print('Largest palindrome is %d' % largest_possible_palindrome(1000))

if __name__ == '__main__':
    main()
