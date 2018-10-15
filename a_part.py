import numpy as np
import matplotlib.pyplot as plt
import matplotlib

mean = 0
sigma = 3.0
n = 10000

#  We need 2 random number generators
r1 = np.random.sample(size = n)
r2 = np.random.sample(size = n)

# Introducing these numbers to x and y generators

gen1 = np.sqrt(-2*sigma**2*np.log(1-r1))

x_mean = gen1*np.cos(2*np.pi*r2) + mean


# Ploting of the theoretical and random sample.
    # Theoretical
x1 = np.linspace(-15, 15, 1000)
y1 = 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x1 - mean)**2/(2*sigma**2))
    
    # Random Sample
bins = np.linspace(-15, 15, 31)
plt.hist(x_mean, bins = bins, normed = True, label= 'Random sample')
plt.plot(x1 ,y1,label=r'$p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }} e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} }$')
plt.legend(loc=(0.6, 0.7))
plt.show()






