def get_edits_away(string1, string2):
        x = len(string1)
        y = len(string2)
        table = [[0] * (y + 1) for _ in range(x + 1)]
        for i in range(0,x):
            table[i][0] = i
        for j in range(0,y):
            table[0][j] = j
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if string1[i - 1] == string2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]

def check_if_one_edit_away(string1, string2):
    if get_edits_away(string1, string2) > 1:
        return False
    else:
        return True

print(check_if_one_edit_away("pale", "ple"))
print(check_if_one_edit_away("pales", "pale"))
print(check_if_one_edit_away("pale", "bale"))
print(check_if_one_edit_away("pale", "bake"))


# Referenced https://skerritt.blog/dynamic-programming/ to read about dynamic progamming in python