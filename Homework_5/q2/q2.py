punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def remove_punctuation(inputstring):
    for i in punctuations:
        inputstring = inputstring.replace(i, "")
    print(inputstring)
    
remove_punctuation("Hello in 36-650, & other MSP courses.")

# Used https://www.w3schools.com/python/ref_string_replace.asp for replace function documentation