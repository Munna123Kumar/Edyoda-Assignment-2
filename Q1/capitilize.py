#Python program to capitalize the first and last character of each word in a string (input string should be a statement)
def word_both_cap(str):
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(),s.title().split()))

s = "Python is a high level programming language"
print("String before:", s)
print("String after:", word_both_cap(str))