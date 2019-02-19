infile = open(r"C:\Users\sjhon\Documents\PythonScripts\Springer\Fah.txt", 'r')

for _ in range(3):
    infile.readline()

Fah = []    
for line in infile.readlines():
    Fah.append(line.split()[-1])

for value in Fah:
    F = float(value)
    C = 5/9*F - 160/9
    print("%.1fF is %.1fC"%(F, C))

infile.close()

