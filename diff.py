import numpy as np
import matplotlib.pyplot as plt

#Bring in the data file:

filename = np.loadtxt('resultat_icomposes_100mil.txt', comments="#", delimiter=",", unpack=False)

#GET THE DIFFERENCE BETWEEN VALUES:

y = [x - filename[i-1] for i, x in enumerate(filename) if i>0]

print '...........Done with computation...........'

#print y
#Save the new data in file:

file = open('calculated_difference'+'.txt', 'w')
file.write(str(y))
file.close()

#diff = np.loadtxt('calculated_difference.txt', comments="#", delimiter=",", unpack=False)

#Now the plotting:
print '............Creating the plot............'
plt.hist(y)
plt.show()
plt.savefig('the_diff_plot.pdf', bbox_inches='tight')
plt.close()

    
    
