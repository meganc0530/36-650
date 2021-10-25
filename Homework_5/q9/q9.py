def check_palindrome(string):
    if len(string) < 1:
        print(True)
    else:
        if string[0] == string[-1]:
            return(check_palindrome(string[1:-1]))
        else: 
            print(False)

check_palindrome("kayak")
check_palindrome("hello")