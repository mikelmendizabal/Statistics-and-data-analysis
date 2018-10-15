import numpy as np
import matplotlib as plt
import functions as fnc # Module we've created for the gaussian number generator
import matplotlib.pyplot as plt
from scipy.special import gamma, factorial

mean = 5.0
sigma = 0.1
n = 1000

matrix = np.ones((5, n))
mean_sample = np.ones(n)
s_sample = np.ones(n)


for i in range (0, n):
    matrix[:,i] = fnc.gen(mean, sigma, 5)
    mean_sample[i] = 1/5* np.sum(matrix[:,i])
    s_sample[i] = np.sqrt(1/(5*(5-1))*np.sum((matrix[:,i]-mean_sample[i])**2))
    
t_sample = (mean_sample - mean)/s_sample
# Theoretical expression of student's t distrubution
t = np.linspace(-8, 8, 1000)
f = 4
t_student = gamma((f+1)/2)/(gamma(f/2)*np.sqrt(np.pi*f))*(1+t**2/f)**(-(f+1)/2)
# Ploting t student variables in histogram
plt.hist(t_sample, bins=51, label='Random sample',normed=True)
plt.plot(t, t_student, label = "Student's t theoretical")
plt.legend(loc=(0.6, 0.7))
plt.show()








