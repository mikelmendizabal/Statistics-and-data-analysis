import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, factorial
import scipy.integrate as integrate


mean = 4.9
x_sample = np.array([4.99252, 5.00079, 4.95892, 5.13911, 4.90149])
n = x_sample.size
sample_mean = 1/n*np.sum(x_sample)
s = np.sqrt(1/(n*(n-1))*np.sum((x_sample-sample_mean)**2))
t_samp = (sample_mean-mean)/s
print("t_sample = ",  t_samp)
f = 4
def studentt (t):
    return ((gamma((f+1)/2))/(gamma(f/2)*np.sqrt(np.pi*f)))*(1+(t**2/f))**(-(f+1)/2)

result, errs = integrate.quad(studentt, t_samp, np.inf)
print("Integral value for the t_sample = ", result)

tot, errs = integrate.quad(studentt, -np.inf, np.inf)
print("The consistency of our guess", 2*result/tot *(100))






