# Exercise 2

a = [[1, 2, 3], [4, 5, 6]]

answer = []
for i in a:
    for j in i:
        answer.append(j)

# Exercise 3

answer = []
for i in [0, 1, 2]:
    tmp = []
    for j in [10, 11, 12]:
        tmp.append(j + (i*3))
    answer.append(tmp)    

# Exercise 4

a = [['Tom', 'Billy', 'Jefferson', 'Wesley'], ['Susie', 'Eva', 'stephanie']]

answer = [name for nameList in a for name in nameList if name.count('e') >= 2]