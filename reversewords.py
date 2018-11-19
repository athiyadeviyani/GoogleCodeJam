def reverseWords(string):
    wordsArray = string.split()
    n = len(wordsArray)
    reversedWordsArray = reversed(wordsArray)
    result = ""
    for i in reversedWordsArray:
        result = result + i + " "
    result = result[:-1]
    return result
    
print(reverseWords("this is a test")) # test a is this
print(reverseWords("foobar")) # foobar
print(reverseWords("all your base")) # base your all
