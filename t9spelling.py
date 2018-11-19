def t9spelling(string):
    keys = {}
    keys[0] = ' '
    keys[2] = 'abc'
    keys[3] = 'def'
    keys[4] = 'ghi'
    keys[5] = 'jkl'
    keys[6] = 'mno'
    keys[7] = 'pqrs'
    keys[8] = 'tuv'
    keys[9] = 'wxyz'
    result = ""
    for char in string:
        presses = 0
        for number in keys.keys():
            if char in keys[number]:
                presses = keys[number].index(char)+1
                if result != "" and result[len(result) - 1] == str(number):
                    result += " " + str(number)*presses
                else:
                    result += str(number)*presses

    return result

if __name__ == '__main__':
    n = int(input())
    for n_itr in range(n):
        print(t9spelling(input()))
 
 # hi = 44 444
 # yes = 999337777
 # foo  bar = 333666 6660 022 2777
 # hello world = 4433555 555666096667775553
