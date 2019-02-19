def extractData(filename):
    infile = open(filename, 'r')
    infile.readline()
    months = []
    rainfall = []
    for line in infile:
        print(line)
        words = line.split()
        months.append(words[0])
        rainfall.append(words[1])
    infile.close()
    months = months[:-1]
    annualAvg = rainfall[-1]
    rainfall = rainfall[:-1]
    return months, rainfall, annualAvg

months, values, avg = extractData('rainfall.txt')    
print('The average rainfall for the months:')
for month, value in zip(months, values):
    print(month, value)
print('The average rainfall for the year:', avg) 

data = [[ 0.75, 0.29619813, -0.29619813, -0.75 ],
    [ 0.29619813, 0.11697778, -0.11697778, -0.29619813],
    [-0.29619813, -0.11697778, 0.11697778, 0.29619813],
    [-0.75, -0.29619813, 0.29619813, 0.75 ]]   

outfile = open('tmpTable.dat', 'w')
ncolumns = len(data[0])
outfile.write('          ')
for i in range(1, ncolumns+1):
    outfile.write("%10s    "%("column %2d"%i))   
outfile.write('\n')
rowCounter = 1
for row in data:
    outfile.write('row %2d'%rowCounter)
    for column in row:
        outfile.write('%14.8f'%column)
    outfile.write('\n')
    rowCounter += 1
outfile.close()

    