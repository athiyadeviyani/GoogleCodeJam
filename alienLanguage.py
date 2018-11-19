def alienLanguage(sentence, language):
    count = 0
    lingo = []
    if '(' not in language:
        for word in sentence:
            if word == language:
                count += 1
    else:
        l = language.split(')')
        for word in l:
            if '(' in word:
                lingo.append(word[1:])
            else:
                for char in word:
                    lingo.append(char)
        flags = []
        for word in sentence:
            flag_local = []
            flag = False
            for i in range(len(word)):
               # print(word[i] + "/" + lingo[i])
                if word[i] in lingo[i]:
                    flag_local.append(True)
                else:
                    flag_local.append(False)
            flags.append(flag_local)
       # print(flags)
        count = len(strings)
        for group in flags:
            if False in group:
                count -= 1      
    return count

if __name__ == "__main__":
    ldn = input().split()
    l = int(ldn[0])
    d = int(ldn[1])
    n = int(ldn[2])
    sentences = []
    for i in range(d):
        sentences.append(input())
    for i in range(n):
        print(alienLanguage(sentences, input()))
        

    '''
    3 5 4
    abc
    bca
    dac
    dbc
    cba
    (ab)(bc)(ca) ----------- outputs 2
    abc -------------------- outputs 1
    (abc)(abc)(abc) -------- outputs 3
    (zyx)bc ---------------- outputs 0
    '''
 
