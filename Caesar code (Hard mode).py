# The program codes all inputting words by Caesar cipher. Shift == lenght of the word.

string = input().split()

def count(step):
    counter = 0
    for i in step:
        if i.isalpha() == True:
            counter += 1
    return counter

result = []
for i in range(len(string)):
    res = []
    for j in string[i]:
        if j.isalpha() == True:
            if j == j.lower():
                decr = ord(j) + count(string[i])
                if decr > 122:
                    decr -= 26
                res.append(chr(decr))
            if j == j.upper():
                decr = ord(j) + count(string[i])
                if decr > 91:
                    decr -= 26
                res.append(chr(decr))
        if j.isalpha() == False:
            res.append(j)
    result.append(res)
for l in result:
    m = ''.join(l)
    print(m, end=' ')


