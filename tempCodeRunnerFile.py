 in range(n):
        if j == start or j == end:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    start += 1
    end -= 1