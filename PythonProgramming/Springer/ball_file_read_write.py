data = open(r"C:\Users\sjhon\Documents\PythonScripts\Springer\data.txt",'r')

v0 = data.readline()
v0 = float(v0.split()[-1])
ignore = data.readline() #ignores the second line of the file, which is "t: "

t = []
for line in data.readlines():
    t += line.split()

data.close()    

g = 9.81
y = lambda t: v0*t - 0.5*g*t**2

outfile = open(r"C:\Users\sjhon\Documents\PythonScripts\Springer\ball_result.txt", 'w')

outfile.write("    t      y(t)\n")
for t_val in t:
    t_val = float(t_val)
    outfile.write("%.6f %.6f\n"%(t_val,y(t_val)))

outfile.close()    

