def storeCredit(credit, items):
    list = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j:
                if items[i] + items[j] == credit:
                    if (items.index(items[i]) + 1) not in list:
                        list.append(items.index(items[i]) + 1)
                    if (items.index(items[j]) + 1) not in list:
                        list.append(items.index(items[j]) + 1)
    result = ' '.join(map(str,list))
    return(result)

if __name__ == "__main__":
    testcases = int(input())
    for testcase in range(testcases):
        credit = int(input())
        no_of_items = int(input())
        items = input().split()
        finalitems = []
        for i in items:
            finalitems.append(int(i))
        print(storeCredit(credit, finalitems))

# 100, [50, 25, 75] = 2 3
# 200, [150,24,79,50,88,345,3] = 1 4
