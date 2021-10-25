def print_triangles(r):
    if (not isinstance(r, int)):
        print("Invalid Input")
    
    elif (r < 0):
        print("Invalid Input")  
    else:
        count = 1
        for i in range(0, r):
            for j in range(0, i + 1):
                print(count, end = " ")
                count = count + 1
            print("\r")

print_triangles(3)
print_triangles(6)
print_triangles(-1)
print_triangles(1.5)

# Used https://www.codespeedy.com/how-does-carriage-return-work-in-python/ to understand carriage returns
