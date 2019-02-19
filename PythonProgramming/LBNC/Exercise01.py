#Exercise 1 - 'For'
even_sum = 0
for i in range(2, 101, 2):
    even_sum += i
    print(i, even_sum)

#Exercise 1 - 'While'
i = 0
even_sum = 0
while i < 100:
    i += 2
    even_sum += i
    print(i, even_sum)    

#Exercise 2
a = ['cat', 'tiger', 'elephant']
for name in a:
    if len(name) > 3:
        print(name)

#Exercise 3
s = 0
for i in range(1, 31):
    if i <= 10 or i >= 20:
        s += i
        print(i, s)

s = 0
i = 0
while i < 30:
    i += 1
    if 10 < i < 20:
        continue
    s += i
    print(i, s)

#Exercise 4
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("total = ", sum(X))
for x in X:
    if 4 <= x < 7:
        print(x)
print("mean = ", mean/len(X))

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for x in X:
    total += x
    if 4 <= x < 7:
        print(x)
print("total = ", total)
mean = total/len(X)
print("mean = ", mean)

#Exercise 5
Y = [1, 1.0, 1.6, 2, 5.1]
for y in Y:
    if type(y) == int:
        print(y)

for y in Y:
    if type(y) == int:
        print(float(y))       
    elif type(y) == float:
        print(int(y))

s = 0
for y in Y:
    if type(y) == float:
        s += y
print(s)



   