import numpy as np


def gen(mean, sigma, n):
    #  We need 2 random number generators
    r1 = np.random.sample(size = n)
    r2 = np.random.sample(size = n)

    # Introducing these numbers to x and y generators

    gen1 = np.sqrt(-2*sigma**2*np.log(1-r1))

    x = gen1*np.cos(2*np.pi*r2)
    y = gen1*np.sin(2*np.pi*r2)

    x_mean = x + mean


    return x_mean








