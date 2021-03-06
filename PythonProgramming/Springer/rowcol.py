data = [[ 0.75, 0.29619813, -0.29619813, -0.75 ],
        [ 0.29619813, 0.11697778, -0.11697778, -0.29619813],
        [-0.29619813, -0.11697778, 0.11697778, 0.29619813],
        [-0.75, -0.29619813, 0.29619813, 0.75 ]]   

outfile = open('tmpTable.dat', 'w')

ncolumns = len(data[0])
outfile.write('          ')
for i in range(1, ncolumns+1):
    outfile.write("%10s    "%("column %2d"%i))
outfile.write("\n")

for i in range(len(data)):
    outfile.write("row %2d"%(i+1))
    for j in range(len(data[i])):
        outfile.write("%14.8f"%data[i][j])
    outfile.write("\n")

outfile.close()        