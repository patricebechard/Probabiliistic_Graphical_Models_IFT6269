#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: hw1.py
# Author: Patrice Bechard <patricebechard@gmail.com>
# Date: 25.09.2017
# Last Modified: 25.09.2017

import numpy as np
import matplotlib.pyplot as plt
import sys

variance = np.array([])

niter = 10000
samplesize = 5

#c) repeat steps (a) and (b) 10,000 times.
for i in range(niter):
    #a) draw n=5 samples from the standard Gaussian distribution, N(0,1)
    sample = np.random.randn(samplesize)
    #b) using the samples as data, compute the ML estimate mu_hat for the mean
    #   and sigma2_hat for the variance of the Gaussian, as given in Question 3(d) above.
    # (The numpy functions used are exactly the same as the ones given in the homework)
    mu_hat = np.mean(sample)
    sigma2_hat = np.var(sample)
    variance = np.append(variance,sigma2_hat)

#c) (continued) Plot a histogram of the 10,000 estimates of the Gaussian variance
#   parameter to show its empirical distribution.
plt.hist(variance)

freq_bias = np.mean(variance) - 1
freq_variance = np.mean(variance**2) - (np.mean(variance))**2

theo_bias = -1 / (niter*samplesize)
theo_variance = (2 * (niter*samplesize - 1) * 1**2) / (niter*samplesize)**2

print("frequentist bias : %f , frequentist variance : %f"%(freq_bias, freq_variance))
print("theoretical bias : %f , theoretical variance : %f"%(theo_bias, theo_variance))

plt.show()
