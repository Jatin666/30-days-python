no_of_rows =  5
for i in range(no_of_rows):
    print(' '*(no_of_rows-i),end="")
    print(' '.join(map(str,str(11**i))))