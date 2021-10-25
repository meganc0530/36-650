output = [[0, 0, 0],
        [0, 0, 0]]
m = [[10, 8],
        [2, 4],
        [1, 7]]

def transpose(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            output[j][i] = m[i][j]
    for out in output:
        print(out)


transpose(m)