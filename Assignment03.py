# import relevant modules
import math

# define variables and lists
i = 0
x = []
y = []
j = 0 
A = 0 
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0
XT = 0
YT = 0
IXT = 0
IYT = 0 

# define number of polygon vertices
nv = int(input("Number of vertices: "))

if nv < 3:
    nv = int(input("Polygons must have at least 3 vertices, please try again: "))

# input x and y coordinates
else:
    while i < nv:
        i = i + 1
        x.append(int(input(f"input x{i}: "))) 
        y.append(int(input(f"input y{i}: ")))

while j < (nv-1):
    A = 1/2 * (x[j+1] + x[j]) * (y[j+1] - y[j]) + A
    Sx = -1/6 * (x[j+1] - x[j]) * (y[j+1]**2 + y[j] * y[j+1] + y[j]**2) + Sx
    Sy = 1/6 * (y[j+1] - y[j]) * (x[j+1]**2 + x[j] * x[j+1] + x[j]**2) + Sy
    Ix = -1/12 * (x[j+1] - x[j]) * (y[j+1]**3 + y[j+1]**2 * y[j+1] * y[j]**2 + y[j]**3) + Ix
    Iy = -1/12 * (y[j+1] - y[j]) * (x[j+1]**3 + x[j+1]**2 * x[j+1] * x[j]**2 + x[j]**3) + Iy
    j = j+1
    
XT = Sy / A
YT = Sx / A
IXT = Ix - YT**2 * A
IYT = Iy - XT**2 * A

print ("Area: ", A)
print ("Static Moment X: ", Sx)
print ("Static Moment Y: ", Sy)
print ("Moment of Interia X: ", Ix)
print ("Moment of Interia Y: ", Iy)
print ("Moment of Interia XY: ", Ixy)
print ("Xt: ", XT)
print ("Yt: ", YT)
print ("IXT: ", IXT)
print ("IYT: ", IYT)


