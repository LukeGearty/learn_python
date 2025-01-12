def comma_code(list):
    result = ""

    beginning = 0
    end = len(list)

    for i in range(beginning, end):
        if i == end - 1:
            result += str(list[i])
        else:
            result += str(list[i]) + ", "
    
    return result


test = ['apples', 'bananas', 'tofu', 'cats']
test2 = [1, 2, 3, 4]
test3 = ['apple', 4, 'question mark', 4.2]
test4 = [True, False, True]
test5 = []

master_list = [test, test2, test3, test4, test5]

for list in master_list:
    print(comma_code(list))
        