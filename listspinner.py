def counterclockwise(isi):
    # isi = [ [1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 9]]

#expected  0  1  2
#       [0[3, 6, 9],
#         0  1  2
#       1[2, 5, 8],
#         0 1  2
#       2[1, 4, 7]]

    row = (list(zip(*isi)))
    #print(row[0][::-1]) 
    res = (row[::-1])
    return res
print(counterclockwise([ [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]))