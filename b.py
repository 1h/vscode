import io
import numpy
x="1 3\n 4.5 8"        
print(numpy.genfromtxt(io.StringIO(x)))