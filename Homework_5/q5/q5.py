def print_pyramid(r):
    spaces = r - 1
    for i in range(0, r):
        for j in range(0, spaces):
            print(end = " ")
        spaces = spaces - 1
        for k in range(0, i + 1):
            print("*", end = " ")
        print("\r")

print_pyramid(5)

# Used https://www.codespeedy.com/how-does-carriage-return-work-in-python/ to understand carriage returns